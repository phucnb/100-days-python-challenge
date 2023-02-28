from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return "hello world1"

# @app.route('/bye')
# def bye():
#     return "bye"

# @app.route('/<guess>')
# def greet(guess):
#     return f"hello {guess}"


# if __name__ == "__main__":

#     app.run(debug=True)

def decoration_test(function):
    def wrapper():
        print("hello")
        function()
        function()
        print("bye")
    return wrapper


@decoration_test
def test():
    print("aaaa")


test()