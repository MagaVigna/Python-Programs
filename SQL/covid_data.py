'''
Design a DB to keep the Covid data for India. Write a program to display the info such as most affected state, city, age group, etc.
'''

import mysql.connector

#creating a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="magavigna",
  database="covid_data"
)

mycursor=mydb.cursor(buffered=True)

# mycursor.execute("CREATE DATABASE covid_data")

#creating a table
mycursor.execute("CREATE TABLE covid (state VARCHAR(20), no_of_deaths VARCHAR(20),recovered VARCHAR(20), positive_cases VARCHAR(20), age_group VARCHAR(20), date VARCHAR(10))") 

#inserting values into the table
sql = "INSERT INTO covid (state,no_of_deaths,recovered,positive_cases,age_group,date) VALUES (%s, %s,%s,%s, %s,%s)"
val = [
  ('Tamil Nadu', '4500','1500','2000','18-30','2022-05-10'),
  ('Kerala', '7000','1500','2000','20-30','2022-10-02'),
  ('Andhra pradesh', '3800','1500','2000','30-40','2022-03-25'),
  ('Haryana', '4000','1500','2000','18-30','2022-02-01'),
  ('Uttar Pradesh', '900','1500','2000','18-30','2022-11-21'),
  ('Himachal Pradesh', '1500','1500','2000','18-50','2022-03-01'),
  ('Goa', '8900','1500','2000','18-30','2022-05-06'),
  ('Odisha', '4500','1500','2000','18-30','2022-04-05')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "rows was inserted.") 

#printing all the values in the table
print("The data in the covid database:")

mycursor.execute("SELECT * FROM covid")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#printing the state with more deaths
print("The state with more deaths: ")

mycursor.execute("SELECT state FROM covid ORDER BY no_of_deaths DESC")

state_with_more_deaths = mycursor.fetchone()

print(state_with_more_deaths)

#printing the most affected state
print("The most affected state:")

mycursor.execute("SELECT state FROM covid ORDER BY positive_cases DESC")

state_with_more_positive_cases = mycursor.fetchone()

print(state_with_more_positive_cases)

#printing the state with highest number of recovered patients
print("The state with more recovered patients:")

mycursor.execute("SELECT state FROM covid ORDER BY recovered DESC")

state_with_more_recovered_cases = mycursor.fetchone()

print(state_with_more_recovered_cases)

#printing the age group that has been most affected
print("The more affected age group:")

mycursor.execute("SELECT age_group FROM covid ORDER BY age_group DESC")

most_affected_age_group = mycursor.fetchone()

print(most_affected_age_group)

'''
Output:
8 rows was inserted.
The data in the covid database:
('Tamil Nadu', '4500', '1500', '2000', '18-30', '2022-05-10')
('Kerala', '7000', '1500', '2000', '20-30', '2022-10-02')
('Andhra pradesh', '3800', '1500', '2000', '30-40', '2022-03-25')
('Haryana', '4000', '1500', '2000', '18-30', '2022-02-01')
('Uttar Pradesh', '900', '1500', '2000', '18-30', '2022-11-21')
('Himachal Pradesh', '1500', '1500', '2000', '18-50', '2022-03-01')
('Goa', '8900', '1500', '2000', '18-30', '2022-05-06')
('Odisha', '4500', '1500', '2000', '18-30', '2022-04-05')
The state with more deaths:
('Uttar Pradesh',)
The most affected state:
('Tamil Nadu',)
The state with more recovered patients:
('Tamil Nadu',)
The more affected age group:
('30-40',)
'''



