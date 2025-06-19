def safe_divide(numerator,denominator):
  result = numerator/denominator
  try:
      if denominator == 0:
        raise ZeroDivisionError ("Error: Cannot divide by zero.")
      return(f"The result of the division {float(result)}")
  except ValueError:
    return("Error: Please enter numeric values only.")
  

try:
  safe_divide(10,2)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)
except Exception as e:
  print(e)

    

