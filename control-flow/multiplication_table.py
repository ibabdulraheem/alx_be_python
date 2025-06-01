number = int(input("Enter a number to see its multiplication table: "))
z = ""
x = number
for y in range (1,11):
    z = x * y
    print (f"{x} * {y} = {z}")
    y+=1
