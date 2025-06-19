def safe_divide (numerator,denominator ):
  try:
      if denominator == 0:
        raise ZeroDivisionError ("Error: Cannot divide by zero.")
      result = float (numerator)/float(denominator)
      return(f"The result of the division is {result}")
  except ValueError:
    return("Error: Please enter numeric values only.")
  

try:
  safe_divide(2,1)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print(e)

    

