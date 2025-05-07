from flask import render_template, request, redirect, url_for, flash


class CurrencyController:
    def __init__(self, model):
        self.model = model

    def index(self):
        rates = self.model.get_rates()
        return render_template('index.html', rates=rates)

    def update_currencies(self):
        if request.method == 'POST':
            currencies = request.form.get('currencies', '').upper().split()
            valid_currencies = []

            for currency in currencies:
                if len(currency) == 3 and currency.isalpha():
                    valid_currencies.append(currency)
                else:
                    flash(f'Invalid currency code: {currency}', 'error')

            if valid_currencies:
                success = self.model.fetch_rates(valid_currencies)
                if success:
                    flash('Курсы валют успешно обновлены!', 'success')
                else:
                    flash('Не удалось получить данные о курсах валют', 'error')

            return redirect(url_for('index'))

        tracked = self.model.get_tracked_currencies()
        return render_template('update.html', tracked_currencies=tracked)