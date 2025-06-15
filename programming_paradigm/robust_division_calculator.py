def safe_divide(numerator, denominator):
  try:
      numerator= float(input("Enter numerator: "))
      denominator = float(input("Enter denominator: ")) 
      result = numerator / denominator
      print(f"The result of the division is {result}")
  except ZeroDivisionError:
    print("Cannot divide by zero.")
  except ValueError:
    print("invalid number symbol entered")
  except Exception as e:
    print(e)
    

safe_divide("numerator","denominator")