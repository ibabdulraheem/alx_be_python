from datetime import datetime, timedelta

def display_current_datetime():
  global current_date
  now = datetime.now()
  current_date = now.strftime("%Y-%m-%d %H:%M:%S")
  print(current_date)

def calculate_future_date():
  display_current_datetime()
  number_of_days = int(input("Enter the number of days to add to the current date (as an integer): "))
  future_date = (str(timedelta(days=number_of_days)) + current_date).strip("%Y-%m-%d %H:%M:%S")
  print(future_date)
calculate_future_date()
