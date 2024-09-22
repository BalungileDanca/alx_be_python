integer = int(input("Enter the size of the pattern: "))
#for i in range(1, integer+1):
 #   print()
  #  for j in range(1, integer+1):
   #     print("*", end='')
row = 0
while row < integer:
    column = row + 1
    for column in range(1, integer+1):
        print("*", end='')
        column += 1
    row += 1
    print()

