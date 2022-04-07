import random
n = 20
justguess = int(n * random.random()) + 1
guess = 0

while guess != justguess:
    guess = int(input("Enter Number to Guess"))
    if guess > 0:
        if guess > justguess:
            print("value is too big")
        elif guess < justguess:
            print("Value is too small")
        else:
            print("CONGO :) :) --You have made it----")
    else:
        print("Go you coward")
        break

