from flask import Flask
from model import db, CurrencyRates
from controller import CurrencyController


def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)


    with app.app_context():
        db.create_all()


    model = CurrencyRates(app)
    controller = CurrencyController(model)


    app.add_url_rule('/', view_func=controller.index)
    app.add_url_rule('/update', methods=['GET', 'POST'], view_func=controller.update_currencies)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)