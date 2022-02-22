# print the triangle pattern
p = int(input("enter the no.of rows we want:"))
for x in range(0,p):
    for y in range(0,p-x-1):
        print(" ",end="")
    for y in range(0,x+1):
        print("*",end=" ")
    print()