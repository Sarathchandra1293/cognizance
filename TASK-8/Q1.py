#given vector is [10,11,12,13,14]
a=int(input("Give first number\n"))
b=int(input("Give last number\n"))
c=""
d=".  0.  0.  0.  0.  0. "
for i in range(a,b):
    c=c+str(i)+d
print(c + str(b))
