from datetime import datetime, timedelta

def disply_current_datetime():
  global current_date
  current_date = datetime.now()
  print(current_date)

def calculate_future_date():
  disply_current_datetime()
  number_of_days = int(input("Enter the number of days to add to the current date (as an integer): "))
  future_date = (current_date + timedelta(days = number_of_days)).strftime("%Y - %m - %d")
  print(future_date)
calculate_future_date()
