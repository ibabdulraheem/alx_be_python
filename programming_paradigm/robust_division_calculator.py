def safe_divide(numerator,denominator):
  try:
      if float(denominator) == 0:
        return("Error: Cannot divide by zero.")
      else:
        return(f"The result of the division is {float(numerator)/float(denominator)}")
  except ValueError:
    return("Error: Please enter numeric values only.")
  

try:
  safe_divide(2,1)
except ZeroDivisionError as e:
  print(e)
except ValueError as e:
  print(e)


    

