secret = 24
guess = 0
limit = 4

while guess < limit:
    think = int(input("Please enter value!"))
    guess = guess + 1
    if think == secret:
        print("You lost")
        break
else:
    print("Try again")
