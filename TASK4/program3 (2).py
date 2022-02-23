str = []
p = int(input("Enter number of elements : "))
print("Enter the roll number , name and marks of user")
for i in range(0, p):
    data = [input(), input(),input()]
    str.append(data)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for x in range(0,3):
    print(str[1][i], end=" "*10)

