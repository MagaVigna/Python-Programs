import mysql.connector

#creating a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="magavigna",
  database="random_data"
)


mycursor=mydb.cursor(buffered=True)

#creating a table
#mycursor.execute("CREATE TABLE hello100(Hello VARCHAR(20))") 

#inserting values
for num in range(0,100):
  value_list=[["Hello"]]
  sql="INSERT INTO hello100 (Hello) VALUES (%s)"
  mycursor.executemany(sql, value_list)

mydb.commit()

print("The data in the database:")

#printing all the data in the table hello100
mycursor.execute("SELECT * FROM hello100")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

