from flask import Flask,render_template,request
import mysql.connector
import json


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
def get_foodtype():
    details=[]
    mycursor.execute("SELECT * FROM project.food_type")
    myresult = mycursor.fetchall()
    for index in myresult:
        details.append(index)
    return details


@app.route("/foodname")
def get_foodname():
    details=[]
    mycursor.execute("SELECT * FROM project.food_calorie_details")
    myresult = mycursor.fetchall()
    for index in myresult:
        details.append(index)
    return details


@app.route("/submituserdetails",methods=["POST"])
def submitting_user_details():
    age=request.form.get("age")
    name=request.form.get("name")
    weight=request.form.get("weight")
    height=request.form.get("height")
    gender=request.form.get("gender")
    username=request.form.get("username")
    password=request.form.get("password")
    dob=request.form.get("dob")
    sql = '''INSERT INTO project.user_details (age,name,weight,height,gender,username,password,dob ) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
    detail=[age,name,weight,height,gender,username,password,dob]
    mycursor.execute(sql, detail)
    mydb.commit()
    return ''


@app.route("/submitFoodDetails", methods=["POST"])
def submitting_food_details():
    username=request.form.get("username")
    type=request.form.get("type")
    name=request.form.get("name")
    quantity=request.form.get("quantity")
    date=request.form.get("date")
    sql = '''INSERT INTO project.user_calorie_intake_details (food_calorie_detail_id,food_type_id,quantity,date,user_details_id) 
    values(%s,%s,%s,%s,
        (SELECT id
        FROM user_details
        WHERE user_details.username=%s))'''
    detail=[name,type,quantity,date,username]
    mycursor.execute(sql, detail)
    mydb.commit()
    return ''


@app.route("/signup", methods =['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/calorie')
def calorie():
    return render_template('calorie_input.html')


@app.route('/submitinlogin',methods=['GET','POST'])
def submitlogin():
    # username = request.form.get('username')
    # password = request.form.get('password')
    # mycursor.execute('SELECT username FROM project.user_details')
    # dbUsername=mycursor.fetchone()
    # mycursor.execute('SELECT password FROM project.user_details ')
    # dbpassword=mycursor.fetchone()
    # if username==dbUsername and password==dbpassword:
    #     return render_template('login.html')
    details=[]
    sql=mycursor.execute("SELECT username,password FROM project.user_details")
    myresult = sql.fetchall()
    for index in myresult:
        details.append(index)
    return details
    

@app.route("/home")
def get_home():
    return render_template("home.html")


@app.route("/options")
def option():
    return render_template('optionpage.html')


@app.route("/add")
def returnadd():
    return render_template("addnewfood.html")


@app.route("/addfooddetails",methods=["POST"])
def add_food_details(): 
    name=request.form.get("name")
    calories=request.form.get("calories")
    foodtypeid=request.form.get("foodtypeid")
    sql = '''INSERT INTO project.food_calorie_details (food_name,calories,food_type_id) values(%s,%s,%s)'''
    detail=[name,calories,foodtypeid]
    mycursor.execute(sql, detail)
    mydb.commit()

    return ''


@app.route("/plot")
def progress_graph():
    return render_template("plot4.html")


@app.route("/dataForPlot")
def getting_data_for_graph():
    sql=mycursor.execute('''SELECT date,food_calorie_details.calories * user_calorie_intake_details.quantity AS total_calories_consumed
                        FROM user_calorie_intake_details 
                        INNER JOIN project.food_calorie_details 
                        ON user_calorie_intake_details.food_calorie_detail_id = food_calorie_details.id
                        INNER JOIN project.user_details
                        ON user_calorie_intake_details.user_details_id = user_details.id''')
    myresult = sql.fetchall()
    # labels = [row[0].strftime("%B") for row in myresult]
    # values = [row[1] for row in myresult]
    # headers = {
    #     "Access-Control-Allow-Origin": "*",
    #     "Access-Control-Allow-Methods": "GET",
    # }
    # return jsonify({
    # 'labels': labels,
    # 'values': values
    # }), 200, headers
    # # return labels,values, 200, headers
    data_json = [{'month': d[0].strftime("%B"), 'calories': d[1]} for d in myresult]

    # Return JSON data
    return json.dumps(data_json)


app.run()