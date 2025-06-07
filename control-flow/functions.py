# LAMDA IMPLEMENTATION
# name = input("Enter your name please: ")
# age = input("Enter your age please: ")
# user_details = lambda name, age: f"if your name is {name}, your age is {age} "
# user = user_details (name,age)
# print(user)

# CALCULATION OF AREA WHEN WIDTH IS GIVEN A DEFAULT VALUE OF 1
# def calculate_area(length, width = 1):
#   length = int(input("Enter length: "))
#   width = int(input("Enter width: "))
#   area = (length)*(width)
#   if width == 1:
#     return length
#   else:
#     return area 
# result = calculate_area(length="length",width="width")
# print(f"Area of the material is : {result}")

# FUNCTION WITH DEFAULT VALUE
# def greetings(name = "Wold"):
#   print(f"hello, {name}")
# greetings()
# greetings("Ibrahim")

# USING GLOBAL KEYWORD WITHIN A FUNCTION TO MODIFY GLOBAL VARIABLE
# count = 0
# def increment_global():
#   global count
#   count += 1
# increment_global()
# print(count)  # Output: 1 (Global count is modified)


# def outer_function():
#     x = 10  # Variable in the enclosing function
#     def inner_function():
#         nonlocal x  # Using nonlocal to modify x from the enclosing function
#         x += 5  # Modifying the value of x
#         inner_function()  # Calling the nested function
#         print("Modified value of x from inner function:", x)
#         outer_function()

# def greet (name):
#   print (f"Hello,{name}")
# greet ("Ibrahim")

# def area_of_rectangle (length, width):
#   area = length * width
#   print(f"area: {area}")
#   return area
# area_of_rectangle (5,4)

# def even_number (number):
#   if number % 2 == 0:
#     print(f"The {number} is even number")
#   else:
#     print(f"the {number} is an odd number")
# even_number(5)

# LIST OPERATION
# my_list = [10,20,30,40,50]
# result1 = my_list[1:4] # Accessing elements of a list from index 1 to 3
# result2 = my_list[::2] # Accessing elements of a list using step 2
# result3 = my_list[::-1] # Reverses the order of a list
# print(result1)
# print(result2)
# print(result3)

# Appending : Adding element(s) to the end of the list

#Removing element from list
# result5 = my_list.remove(60)
# print(result5)

# # Dictionary get(key, default), keys(),values(),items()
# my_dict = {"name":"Ibrahim","Age":42, "Organization":"NEMA","address":"nasarawa"}
# dictionary_value = my_dict.get("Organization")
# print(dictionary_value)
# dictionary_keys = my_dict.keys()
# dictionary_values = my_dict.values()
# dictionary_items = my_dict.items()
# print(dictionary_keys)
# print(dictionary_values)
# print(dictionary_items)

# fovorite_fruits = ["orange","apple","banana","watermelon"]
# most_favorite_fruit = fovorite_fruits[1]
# print(most_favorite_fruit)

# favorite_book = {"title":"mathematical method","author":"lagranja","genre":"science"}
# title_value = favorite_book.get("title")
# title_values = favorite_book.values()
# title_keys = favorite_book.keys()
# title_items = favorite_book.items()
# print(title_value)
# print(title_values)
# print(title_keys)
# print(title_items)


# import calculator
# result= calculator.sub(5,3)
# print(result)

count = 10
def outer_function():
  count = 5
  def inner_function():
    count = 2
    print (count)
  inner_function()
  print(count)
outer_function()

print(count)