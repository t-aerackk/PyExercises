#Strings are the sequence of characters
# A="Anjal"
# B='Thapa'
# print(A+B) #Str interpolation
# print(A+B, len(A+B)) #length of multiple string
# C= ''' In programming, a string is a sequence of characters. 
# It is a data type used to represent text in various programming languages, 
# including Python.
# Strings are typically used to store and manipulate textual 
# data such as names, sentences, or any other collection of characters.'''
# # print(C, len(C)) #multi line string with length 
# print(A[0],[1],[2],[3],[4]) #Accessing data on indices
# print(A[1:5]. upper()) #String slice
# if "Ans" in C: #Checking items
#     print("Its present")
# else:
#     print("Its not")

price=175
quantity=20
total=price*quantity
myorder="I want {} litre of petrol of {} rs which will amount to {}"
print(myorder.format(quantity,price,total))
alt="Hello brother please fill me {2} rupees of petrol  at rupees{1} which will amount to {0} litres "
print(alt.format(quantity,price,total))
