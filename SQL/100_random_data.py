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
mycursor.execute("CREATE TABLE hello(Hello VARCHAR(20), count VARCHAR(10))") 

#inserting values
for num in range(0,100):
  value_list=[["Hello",num+1]]
  sql="INSERT INTO hello (Hello,count) VALUES (%s,%s)"
  mycursor.executemany(sql, value_list)

mydb.commit()

print("The data in the database:")

#printing all the data in the table hello
mycursor.execute("SELECT * FROM hello")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("DROP TABLE hello")
'''
Output"
The data in the database:
('Hello', '1')
('Hello', '2')
('Hello', '3')
('Hello', '4')
('Hello', '5')
('Hello', '6')
('Hello', '7')
('Hello', '8')
('Hello', '9')
('Hello', '10')
('Hello', '11')
('Hello', '12')
('Hello', '13')
('Hello', '14')
('Hello', '15')
('Hello', '16')
('Hello', '17')
('Hello', '18')
('Hello', '19')
('Hello', '20')
('Hello', '21')
('Hello', '22')
('Hello', '23')
('Hello', '24')
('Hello', '25')
('Hello', '26')
('Hello', '27')
('Hello', '28')
('Hello', '29')
('Hello', '30')
('Hello', '31')
('Hello', '32')
('Hello', '33')
('Hello', '34')
('Hello', '35')
('Hello', '36')
('Hello', '37')
('Hello', '38')
('Hello', '39')
('Hello', '40')
('Hello', '41')
('Hello', '42')
('Hello', '43')
('Hello', '44')
('Hello', '45')
('Hello', '46')
('Hello', '47')
('Hello', '48')
('Hello', '49')
('Hello', '50')
('Hello', '51')
('Hello', '52')
('Hello', '53')
('Hello', '54')
('Hello', '55')
('Hello', '56')
('Hello', '57')
('Hello', '58')
('Hello', '59')
('Hello', '60')
('Hello', '61')
('Hello', '62')
('Hello', '63')
('Hello', '64')
('Hello', '65')
('Hello', '66')
('Hello', '67')
('Hello', '68')
('Hello', '69')
('Hello', '70')
('Hello', '71')
('Hello', '72')
('Hello', '73')
('Hello', '74')
('Hello', '75')
('Hello', '76')
('Hello', '77')
('Hello', '78')
('Hello', '79')
('Hello', '80')
('Hello', '81')
('Hello', '82')
('Hello', '83')
('Hello', '84')
('Hello', '85')
('Hello', '86')
('Hello', '87')
('Hello', '88')
('Hello', '89')
('Hello', '90')
('Hello', '91')
('Hello', '92')
('Hello', '93')
('Hello', '94')
('Hello', '95')
('Hello', '96')
('Hello', '97')
('Hello', '98')
('Hello', '99')
('Hello', '100')'''