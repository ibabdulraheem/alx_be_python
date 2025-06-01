user = int(input("Enter the size of the pattern: "))
i = 1
while i <= user:
  j = 1
  for j in range(user):
    print("*",end="")
    j+=1
  print()
  i+=1