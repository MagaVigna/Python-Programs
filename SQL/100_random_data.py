import mysql.connector

#creating a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="magavigna",
  database="random_data"
)

value_list=["Hello"]
val=[]

mycursor=mydb.cursor(buffered=True)

#creating a table
mycursor.execute("CREATE TABLE hello (Hello VARCHAR(20))") 

#inserting values
sql = "INSERT INTO hello (Hello) VALUES (%s)"

#appending the word hello into the list val
for loop in range(0,100):
    val.append(value_list)

mycursor.executemany(sql, val)

mydb.commit()

print("The data in the database:")

#printing all the data in the table hello
mycursor.execute("SELECT * FROM hello")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''
Output"
The data in the database:
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)
('Hello',)'''