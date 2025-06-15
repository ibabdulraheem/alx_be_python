def safe_divide(numerator, denominator):
  try:
      numerator= int(input("Enter numerator: "))
      denominator = int(input("Enter denominator: "))
      print(numerator/denominator)
  except ZeroDivisionError:
    print("Division by zero is not possible")
  except ValueError:
    print("invalid number symbol entered")
  except Exception as e:
    print(e)
    

safe_divide("numerator","denominator")