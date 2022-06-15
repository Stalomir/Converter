from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import bank

@app.route("/converter/", methods=["GET", "POST"])
def converter():
    codes = []
    for rate in bank.rates:
        codes.append(rate['code'])
    if request.method == 'GET':
        return render_template("currency_calc.html", codes=codes)
    if request.method == 'POST':
        data = request.form
        code = data.get('code')
        amount = data.get('amount')
        for rate in bank.rates:
            if code == rate['code']:
                price = round(float(amount)*(rate['ask']),2)
        return render_template("currency_calc.html", codes = codes, price = price, amount = amount, code = code)

    