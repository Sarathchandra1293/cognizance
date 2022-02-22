store = [ [1,'abc',90],
         [2,'bcd',95],
         [3,'def',85] ]

print("{:<9} {:<9} {:<9}".format('Roll No','Name','Marks'))
for x in range(0,3):
    print(store[1][x],end=" "*9)
