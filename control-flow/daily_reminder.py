task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
  case "high":
    if priority == "high" and time_bound == "yes":
      print (f"Reminder: {task} is a {priority} periority task that requires immediate attention today!")
  case "medium":
    if priority == "medium" and time_bound == "yes":
      print(f"Reminder: {task} is a {priority} periority task that requires your attension when you are less buzy today or later!")
  case "low":
    if priority == "low" and time_bound == "no":
      print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time")
  case _:
    print("The task requires no attesion!")