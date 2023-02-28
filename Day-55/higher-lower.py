from flask import Flask
from random import randint

app = Flask(__name__)

number = randint(0, 9)

print(number)

@app.route('/<int:num>')
def guess_number(num):
    if num == number:
        return '<h1> correct</h1>'
    if num < number:
        return '<h2>too low</h2>'
    else:
        return '<h2>too high</h2>'

if __name__ == "__main__":
    app.run(debug=True)