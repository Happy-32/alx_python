from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number.html', number=n)
    else:
        return 'Invalid input. Please provide an integer.'

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template('number_odd_or_even.html', number=n, parity='even')
        else:
            return render_template('number_odd_or_even.html', number=n, parity='odd')
    else:
        return 'Invalid input. Please provide an integer.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
