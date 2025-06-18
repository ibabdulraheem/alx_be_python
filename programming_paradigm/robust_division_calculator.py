def safe_divide (numerator,denominator ):
  try:
      result = float(numerator) / float(denominator)
      print ( f"The result of the division is {result}" )
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError:
    print("Error: Please enter numeric values only.")
  except Exception:
    print("Please enter numeric values only.")

try:
  safe_divide(6,2)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print(e)

    

