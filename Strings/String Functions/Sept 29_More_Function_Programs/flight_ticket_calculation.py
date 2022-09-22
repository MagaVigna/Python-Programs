'''3.Calculate the cost flight tickets. Single one way ticket from Madurai to Chennai (or vice versa) is Rs 3500 for
 weekday morning and afternoon flights. Rs 3000 for weekday evening flights. Rs 5000 for weekends. Senior discout is 10%.
 Tickets bought at least two weeks ahead of time is 20% off.
 Print the number of weekend tickets sold in a given day.'''

from datetime import date, datetime
from xmlrpc.client import DateTime

weekday_mrng_and_afternoon_ticket=3500 #hardcoding tickets costs
weekday_evening_ticket=3000
weekend_ticket=5000
isweekend=0 #to check whether day is weekend or weekday
isweekday=0
senior_age=60 #hard coding senior's age value
total_ticket=0
number_of_weekend_tickets=0

def weekday_or_weekend_calculation(): #function that checks whether the entered date is weekday or weekend
    global flight_date,isweekday,isweekend
    flight_date=datetime(year,month,dat)
    if flight_date.weekday()<=4:
        isweekday=1
    else:
        isweekend=1

def number_of_days_calculation(): #function to calculate the number of days between the booking date and the flight ticket date
    global ticket_booking_date,no_of_days,flight_date
    flight_date=date(year,month,dat)
    ticket_booking_date=date.today()
    no_of_days=(ticket_booking_date-flight_date).days

def user_details():
    global age,year,month,dat,hour
    age=int(input("Enter your age:")) #getting input from the users
    booking_date=input("Enter the date of flight: (dd/mm/yyyy) : ")
    split_date=booking_date.split("/")
    year=int(split_date[2])
    month=int(split_date[1])
    dat=int(split_date[0])
    time_flight=input("Enter the time of the flight: (24 hours, 00:00) :")
    split_time=time_flight.split(":")
    hour=int(split_time[0])

user_details()
weekday_or_weekend_calculation()
if isweekday: #calculating ticket costs
    if(hour>15):
        total_ticket+=weekday_mrng_and_afternoon_ticket
    else:
        total_ticket+=weekday_evening_ticket
elif isweekend:
    total_ticket+=weekend_ticket
    number_of_weekend_tickets+=1

number_of_days_calculation()
if(abs(no_of_days)>=14): #calculating discounts
    total_ticket-=total_ticket*0.2
if(age>=senior_age):
    total_ticket-=total_ticket*0.1

print("The flight ticket cost is:",total_ticket)
print("Number of weekend tickets sold is: ",number_of_weekend_tickets)

'''
Output:
Enter your age:20
Enter the date of flight: (dd/mm/yyyy) : 10/10/2022
Enter the time of the flight: (24 hours, 00:00) :12:00
The flight ticket cost is: 2400.0
Number of weekend tickets sold is:  0'''

'''
Enter your age:70
Enter the date of flight: (dd/mm/yyyy) : 01/10/2022
Enter the time of the flight: (24 hours, 00:00) :12:00
The flight ticket cost is: 4500.0
Number of weekend tickets sold is:  1'''