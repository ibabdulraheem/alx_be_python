from datetime import datetime, timedelta

def display_current_datetime():
  global current_date
  now = datetime.now()
  current_date = now.strftime("%Y-%m-%d %H:%M:%S")
  print(current_date)
display_current_datetime()

def calculate_future_date():
  number_of_days = int(input("Enter the number of days to add to the current date: "))
  current_date = datetime.now()
  future_date = current_date + timedelta(days=number_of_days)
  print(future_date.strftime("%Y-%m-%d"))
calculate_future_date()
