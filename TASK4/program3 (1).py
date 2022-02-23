str = []
p = int(input("Enter no.of rows : "))
print("Enter roll number , name and marks of a user")
for j in range(0, p):
    data = [input(), input(),input()]
    str.append(data)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for x in str:
    for y in x:
        print(y,end=" "*9)
    print()
