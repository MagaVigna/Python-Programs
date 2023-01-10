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

class user:
    def __init__(self, id, name, age,height,weight,gender,password,dob,username):
        self.id = id
        self.name = name
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.gender=gender
        self.password=password
        self.dob=dob
        self.username=username

@app.route('/users')
def get_users():

    mycursor.execute('SELECT * FROM project.user_details')

    users = []
    for row in mycursor:
        users.append(user(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

    return render_template('userclass.html', users=users)


app.run()