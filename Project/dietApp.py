from flask import Flask,render_template,request,redirect, session, redirect, url_for, jsonify
from flask_login import logout_user, LoginManager
from mysql.connector import cursor
import mysql.connector,json,requests


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="magavigna",
  database="project"
)

mycursor=mydb.cursor(buffered=True)


app=Flask(__name__)
app.secret_key = 'secret'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    result = cursor.var(str, 255)
    mycursor = cursor(prepared=True)
    mycursor.callproc('load_user', (user_id, result))
    mycursor.close()
    return result.getvalue()

    
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/signup", methods =['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route("/foodtype")
def get_foodtype():
    details = []
    mycursor.callproc('get_foodtype')
    stored_results = mycursor.stored_results()
    for result in stored_results:
        myresult = result.fetchall()
        for index in myresult:
            details.append(index)
    return details


@app.route("/foodname")
def get_foodname():
    details = []
    mycursor.callproc('get_foodname')
    stored_results = mycursor.stored_results()
    for result in stored_results:
        myresult = result.fetchall()
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
    mycursor.callproc('submit_user_detail', (age, name, weight, height, gender, username, password, dob))

    # retrieve the result
    result = mycursor.fetchone()
    if result is None:
        message = "No data returned"
    else:
        message = result[0]

    # close the cursor and connection
    mycursor.close()
    mydb.commit()

    
    

    return jsonify({'message': message})



@app.route("/submitFoodDetails", methods=["POST"])
def submitting_food_details():
    if 'username' in session:
        username = session['username']
        type=request.form.get("type")
        name=request.form.get("name")
        quantity=request.form.get("quantity")
        date=request.form.get("date")
        mycursor.callproc('submit_food_details', (username, type, name, quantity, date))
        mydb.commit()
        return ''



@app.route('/calorie')
def calorie():
    if 'username' in session:
        return render_template('calorie_input.html')


@app.route('/submitinlogin', methods=['GET', 'POST'])
def submitlogin():
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = username
    mycursor.callproc('submit_login', (username, password))
    # Fetch the result of the stored procedure
    user = mycursor.fetchall()
    if user is not None:
        return redirect(url_for('option'))
    else:
        # If the credentials are invalid, display an error message
        return render_template('login.html', error='Invalid login')


@app.route("/options", methods=['GET','POST'])
def option():
    if 'username' in session:
        return render_template('mainhome.html')


@app.route("/add")
def returnadd():
    if 'username' in session:
        return render_template("addnewfood.html")

@app.route("/addfooddetails",methods=["POST"])
def add_food_details(): 
    name=request.form.get("name")
    calories=request.form.get("calories")
    foodtypeid=request.form.get("foodtypeid")
    mycursor.callproc('add_food_details', (name, calories, foodtypeid))
    mydb.commit()
    return ''


@app.route("/plot")
def progress_graph():
    if 'username' in session:
        return render_template("plot4.html")


# @app.route("/dataForPlot")
# def getting_data_for_graph():
#     if 'username' in session:
#         username = session['username']
#         mycursor.execute("SET @user_id = NULL;") # registering the output parameter
#         mycursor.execute("SET @username = %s;", (username,)) # passing the input parameter
#         mycursor.execute('CALL getUserId(@username, @user_id);') # calling the stored procedure
#         mycursor.execute('SELECT @user_id;') # fetching the output parameter
#         user_id = mycursor.fetchone()[0]
#         mycursor.callproc('getCaloriesData', (user_id,))
#         myresult = mycursor.fetchall()
#         data_json = [{'day': d[0].strftime("%d %B %Y") if d[0] else "No Data", 'calories': float(d[1])} for d in myresult]
#         return json.dumps(data_json)



@app.route("/dataForPlot")
def getting_data_for_graph():
    if 'username' in session:
        username_list=[]
        username = session['username']
        username_list.append(username)
        mycursor.execute('''SELECT id
            FROM user_details
            WHERE user_details.username=%s''',(username_list))
        userid=mycursor.fetchone()
        sql='''SELECT DATE(date), SUM(food_calorie_details.calories * user_calorie_intake_details.quantity) AS total_calories_consumed
                            FROM user_calorie_intake_details 
                            INNER JOIN project.food_calorie_details 
                            ON user_calorie_intake_details.food_calorie_detail_id = food_calorie_details.id
                            WHERE user_calorie_intake_details.user_details_id = %s 
                            GROUP BY DATE(date)'''
        mycursor.execute(sql,userid)
        myresult = mycursor.fetchall()
        data_json = [{'day': d[0].strftime("%d %B %Y") if d[0] else "No Data", 'calories': float(d[1])} for d in myresult]
        return json.dumps(data_json)


@app.route('/apihome')
def apihome():
    if 'username' in session:
        return render_template('apihome.html')


@app.route('/search')
def search():
  query = request.args.get('query')
  url = "https://api.edamam.com/search"
  params = {
    "q": query,
    "app_id": "501425c3",
    "app_key": "7c297522a9d4afe423a4ea8dcdc1fec6"
  }
  response = requests.get(url, params=params)
  data = response.json()
  return render_template('results.html', data=data)


@app.route('/logout', methods=['POST'])
def logout():
  logout_user()
  return redirect(url_for('home'))


app.run()