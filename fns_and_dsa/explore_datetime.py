from datetime import datetime,timedelta

def display_current_datetime ():
    current_date= datetime.datetime.now()
    print("current date and time is: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

def calculate_future_date ():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date= datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days= number_of_days)
    print("future date is: ", future_date.strftime("%Y-%m-%d"))

calculate_future_date()