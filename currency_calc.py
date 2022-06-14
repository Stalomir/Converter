from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import bank

@app.route("/converter/", methods=["GET", "POST"])
def converter():
    items = []
    for i in bank.rates:
        items.append(i['code'])
    if request.method == 'GET':
        return render_template("currency_calc.html", items=items)
    if request.method == 'POST':
        data = request.form
        currency = data.get('currency')
        amount = data.get('amount')
        for i in bank.rates:
            if currency == i['code']:
                price = round(float(amount)*(i['ask']),2)
                print(currency, price)
        return render_template("currency_calc.html", items = items, price = price, amount = amount, currency = currency)

    