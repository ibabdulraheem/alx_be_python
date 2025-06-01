size_of_pattern = int(input("Enter the size of the pattern (positive integer): "))
i = 1
while i <= size_of_pattern:
  j = 1
  for j in range(size_of_pattern):
    print("*",end="")
    j+=1
  print()
  i+=1