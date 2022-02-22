store = [ [1,'abc',90],
         [2,'bcd',95],
         [3,'def',85] ]

print("{:<9} {:<9} {:<9}".format('Roll No','Name','Marks'))
for x in store:
    for y in x:
        print(y,end=" "*9)
    print()
