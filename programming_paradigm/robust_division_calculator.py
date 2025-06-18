def safe_divide (numerator,denominator ):
  try:
      result = float(numerator) / float(denominator)
      print ( f"The result of the division is {result}" )
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError:
    print("invalid number symbol entered")
  except Exception:
    print("Please enter numeric values only.")

try:
  safe_divide(10,5)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print(e)

    

