def perform_operation(num1,num2,operation):
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
  if operation == "add":
    result = num1 + num2
  elif operation == "subtract":
    result = num1 - num2
  elif operation == "multiply":
    result = num1 * num2
  elif operation == "divide":
    if num2!=0:
      result = num1/num2
    elif num2 == 0:
      result = "Invalid operation"
  print(f"Result: {result}")
perform_operation(1,2,"add")
  