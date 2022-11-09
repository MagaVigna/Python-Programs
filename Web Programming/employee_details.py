from flask import Flask, render_template

app = Flask(__name__)

@app.route('/emp_details')
def emp_temp():
    return render_template('emp.html')

@app.route('/employee/<string:salutation>/<string:firstname>/<string:lastname>/<int:phno>/<string:occupation>/')
def employee(salutation,firstname,lastname,phno,occupation):
    emp = {"Salutation": salutation, 
    "Firstname":firstname,
    "Lastname":lastname,
    "phoneno":phno,
    "Occupation":occupation}
    return emp

app.run()