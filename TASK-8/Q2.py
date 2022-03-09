# Making the 1st array
x = []
p = int(input("Number of elements in array:\n"))
print("Enter the elements of the First array")
for i in range(0, p):
    m = int(input())
    x.append(m)
# Making the 2nd array
y = []
# n=int(input("Number of elements in array:\n"))
print(("Enter the elements of the Second array\n"))
for i in range(0, p):
    m = int(input())
    y.append(m)

print("The Array's are\n")
print(x)
print(y)

if x == y:
    print("\nTrue\n")
else:
    print("\nFalse\n")
