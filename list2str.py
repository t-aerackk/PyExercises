# #converting list to string
list=[]
num_input=int(input("Enter the number of items you want:\n"))
for i in range(num_input):
    num_input=int(input("Enter a number:\n",))
    list.append(num_input)
print(list)

# myList=[str(element) for element in list]
# print(myList)

myList=map(str, list)
result=','.join(myList)
print(result)