def safe_divide  (numerator,denominator ):
  try:
      numerator = float()
      denominator = float()
      # numerator = float(input("Enter Numerator: "))
      # denominator = float(input("Enter Denominator: "))
      result = numerator / denominator
      print(f"The result of the division is {result}")
  except ZeroDivisionError:
    print("Cannot divide by zero.")
  except ValueError:
    print("invalid number symbol entered")
  except Exception:
    print("Please enter numeric values only.")
    

