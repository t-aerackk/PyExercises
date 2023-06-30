#List are multiple items in single variable
A=["A","N","J","A","L"]
# print(len(A), A)
# print(A[1],A[-2])

#list are changable
# A.insert(1,"E") #inserting data on specific location
# print(A)
# A.append("Thapa") #insert on last
# print(A)
# A.remove("Thapa")
B=["T", "H", "A", "P", "A"]
A.extend(B) #Add one list to another
del A[0] #deleting items
print(len(A))
for i in A:
    print(i)