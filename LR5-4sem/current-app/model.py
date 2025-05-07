from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime

db = SQLAlchemy()


class Currency(db.Model):
    __tablename__ = 'currencies'
    code = db.Column(db.String(3), primary_key=True)
    rate = db.Column(db.Float)
    updated_at = db.Column(db.String)


class CurrencyRates:
    _instance = None

    def __new__(cls, app):
        if cls._instance is None:
            cls._instance = super(CurrencyRates, cls).__new__(cls)
            cls._instance.app = app
        return cls._instance

    def fetch_rates(self, currencies):
        with self.app.app_context():
            try:
                response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
                data = response.json()

                for code in currencies:
                    if code in data['Valute']:
                        rate = data['Valute'][code]['Value']
                        currency = Currency.query.get(code)
                        if currency:
                            currency.rate = rate
                            currency.updated_at = datetime.now().isoformat()
                        else:
                            currency = Currency(
                                code=code,
                                rate=rate,
                                updated_at=datetime.now().isoformat()
                            )
                            db.session.add(currency)
                db.session.commit()
                return True
            except Exception as e:
                self.app.logger.error(f"Error fetching rates: {e}")
                db.session.rollback()
                return False

    def get_rates(self):
        with self.app.app_context():
            return {c.code: c.rate for c in Currency.query.all()}

    def get_tracked_currencies(self):
        with self.app.app_context():
            return [c.code for c in Currency.query.all()]