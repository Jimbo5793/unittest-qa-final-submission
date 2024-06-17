from flask import Flask, render_template, request, redirect, url_for
from solution import Solution

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        coins = request.form.get('coins')
        amount = request.form.get('amount')

        try:
            # Convert input to appropriate types
            coins = list(map(int, coins.split(',')))
            amount = int(amount)

            # Instantiate the Solution class and compute result
            solution = Solution()
            result = solution.coin_change(coins, amount)
            return render_template('index.html', result=result, coins=coins, amount=amount)

        except ValueError as e:
            error_message = str(e)
            return render_template('index.html', error=error_message)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
