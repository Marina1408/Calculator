from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("app.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    operation = request.form["operation"]

    if num1 and num2:
        calculator = Calculator(int(num1), int(num2), operation)
        result = calculator.operate()
        return render_template("app.html", result=result)
    else:
        message = "Please enter two numbers"
        return render_template("app.html", result=message)
