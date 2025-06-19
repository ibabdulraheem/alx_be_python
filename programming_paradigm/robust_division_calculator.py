def safe_divide(numerator,denominator):
  try:
      if denominator == 0:
        raise ZeroDivisionError ("Error: Cannot divide by zero.")
      return(f"The result of the division is {float(numerator)/float(denominator)}")
  except ValueError:
    return("Error: Please enter numeric values only.")
  

try:
  safe_divide(2,0)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)


    

