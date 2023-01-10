from flask import Flask,render_template,request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="magavigna",
  database="sayur"
)

mycursor=mydb.cursor(buffered=True)

app=Flask(__name__)


@app.route("/homepage")
def get_index():
    return render_template("proj.html")

@app.route("/displayuserdetails")
def get_users():
    details=[]
    mycursor.execute("SELECT * FROM sayur.tblsampdata")
    myresult = mycursor.fetchall()
    for index in myresult:
        details.append(index)
    return details

@app.route("/getuserdetails", methods=["POST"])
def create_new_user():
    age=request.form.get("age")
    weight=request.form.get("weight")
    height=request.form.get("height")
    sql = "INSERT INTO sayur.tblsampdata (age,weight,height) VALUES (%s, %s,%s)"
    detail=[age,weight,height]
    mycursor.execute(sql, detail)
    mydb.commit()
    return ''

app.run()