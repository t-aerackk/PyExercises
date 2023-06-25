def Rev_Str(string):
    new_str=""
    for char in string:
        new_str=char+new_str
    return new_str

string=input("Enter the string to reverse:")
new_str=Rev_Str(string)
print(f"The rev sdtring is {new_str}")