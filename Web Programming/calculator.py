from flask import Flask, render_template

app = Flask(__name__)

@app.route('/calculator')
def calculator():
    return render_template('calc.html')
    
@app.route('/add/<int:num1>/<int:num2>')
def sum(num1,num2):
    return f'Sum of {num1} and {num2} is {str(num1+num2)}'

@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1,num2):
    return f'Difference of {num1} and {num2} is {str(num1-num2)}'

@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1,num2):
    return f'Product of {num1} and {num2} is {str(num1*num2)}'

@app.route('/div/<int:num1>/<int:num2>')
def div(num1,num2):
    return f'Quotient of {num1} and {num2} is {str(num1/num2)}'

app.run()