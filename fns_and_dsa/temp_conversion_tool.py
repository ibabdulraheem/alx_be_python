FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  celcius = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(celcius)

def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  print(fahrenheit)

user = float(input("Enter the temperature to convert: "))
conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if conversion == "f":
  convert_to_celsius(user)
elif conversion == "c":
  convert_to_fahrenheit(user)
else:
  print("Invalid input! try again")