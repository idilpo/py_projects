# Number guessing game:

import random as rnd # random number generator is imported
secret_num = rnd.randint(1, 100) # range for the random number is given
check = False #checking if numbers match is set to "false" in the beginning

for x in range(5): # the player is given 5 guesses
    user_guess = int(input("Please enter your guess: "))
    if (user_guess == secret_num):
        print("You won!")
        check = True #checking if numbers match is set to "true"
        break

    elif (user_guess < secret_num):
        print("Hint: enter a greater number!")

    else:
        print("Hint: enter a smaller number!")

if not check: # if user's guesses are not right
    print("You lost! :(\nThe number was: ", secret_num)

