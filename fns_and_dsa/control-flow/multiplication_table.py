number = int(input("Enter a number to see its multiplication table: "))
z = ""
for y in range (1,11):
    z = number * y
    print (f"{number} * {y} = {z}")                    # print(x,"*",y,"=",z)
    y+=1
