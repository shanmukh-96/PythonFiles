#write a program to print the duplicates in a list

#Input:
#["hello","10","20","30","20","30","40","50","60","20"]

#Output:
#['20', '30', '20']

l1 = ["hello","10","20","30","20","30","40","50","60","20"]

l2 = []

l3 = []

for c in l1:
    if c in l2:
        l3.append(c)
    else:
        l2.append(c)
        
print(l3)
        