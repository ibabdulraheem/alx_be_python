def safe_divide (numerator,denominator ):
  try:
      result = float(numerator) / float(denominator)
      if denominator ==0:
        raise ZeroDivisionError
      print("Error: Cannot divide by zero.")
  except ValueError:
    print("Error: Please enter numeric values only.")
  except Exception:
    print("Please enter numeric values only.")

try:
  safe_divide(2,1)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print(e)

    

