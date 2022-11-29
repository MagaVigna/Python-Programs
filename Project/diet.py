from flask import Flask,render_template
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="magavigna",
  database="project"
)

mycursor=mydb.cursor(buffered=True)

app=Flask(__name__)


@app.route("/diethome")
def get_index():
    return render_template("calorie_input.html")

@app.route("/foodtype")
def get_users():
    details=[]
    mycursor.execute("SELECT * FROM project.food_type")
    myresult = mycursor.fetchall()
    for index in myresult:
        details.append(index)
    return details

app.run()