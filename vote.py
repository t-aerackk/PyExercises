#Voting appp
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter your correct age")

    if age <= 17:
        print("You are not eligible to vote. Please go home now.")
    elif age >= 100:
        print("I bet it's someone voting for you. Please go home.")
    elif age in range(17, 60):
        print("Please choose the candidate wisely.")
    elif age in range(59, 100):
        print("Please double-check the stamp and proceed. Make sure to fold.")
    else:
        print("Please enter a valid age.")
