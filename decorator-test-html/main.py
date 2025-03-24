from flask import Flask

def make_bold(func):
    def wrapper_function():
        return f"<b>{func()}</b"
    return wrapper_function

def make_emphasis(func):
    def wrapper_function():
        return f"<em>{func()}</em>"
    return wrapper_function

def make_underlined(func):
    def wrapper_function():
        return f"<u>{func()}</u>"
    return wrapper_function

app=Flask(__name__)


@app.route("/")

def hello():
    return ("<h1 style='text-align:center'>Hello, Everyone!</h1>"
            "<p style='text-align:center'>This is Alex</p>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTJmeTJ6bWVrNW9xZTF5cGV3cDY0MG13a3JidXlwMWl6ODFlZnlwMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.gif'/>")

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "good bye"

if __name__=="__main__":
    app.run(debug=True)