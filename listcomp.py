#find even number from a list of numbers entere dby user
list=int(input("Enter number of elements in list"))
a=[]
for num in range(list):
    number=input("Enter elements:")
    a.append(number)
for element in a:
    if element % 2==0:
        print(element)
    else:
        print("ENter even number")