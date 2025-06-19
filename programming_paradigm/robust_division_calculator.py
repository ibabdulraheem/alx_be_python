def safe_divide (numerator,denominator ):
  try:
      result = float(numerator) / float(denominator)
      if denominator == 0:
        raise ZeroDivisionError ("Error: Cannot divide by zero.")
      else:
        (f"The result of the division is {result}")
  except ValueError:
    print("Error: Please enter numeric values only.")
  

try:
  safe_divide(2,0)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print(e)

    

