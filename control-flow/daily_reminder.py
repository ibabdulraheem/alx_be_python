task = input("Enter your task: ")
periority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match periority:
  case "high":
    if periority == "high" and time_bound == "yes":
      print (f"Reminder: {task} is a {periority} periority task that requires immediate attention today!")
  case "medium":
    if periority == "medium" and time_bound == "yes":
      print(f"Reminder: {task} is a {periority} periority task that requires your attension when you are less buzy today or later!")
  case "low":
    if periority == "low" and time_bound == "no":
      print(f"Note: {task} is a {periority} priority task. Consider completing it when you have free time")
  case _:
    print("The task requires no attesion!")