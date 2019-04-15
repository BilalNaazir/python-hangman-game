import random

from pip._vendor.distlib.compat import raw_input

import time

# welcoming the user

def playagain():
    choice = input('Play again? (y/n): ')

    return choice.lower() == 'y'
def playgame():
    name = raw_input("What is your name? ")

    print("Hello, " + name, "Time to play hangman!")

    print(" ")

    # wait for 1 second
    time.sleep(1)

    print("Start guessing...")
    time.sleep(0.5)

    # here we set the secret
    wordList=["secret", "kitchen", "great","distinguish","crave","feather","green","difficult","hard" ]
    word = random.choice(wordList)

    # creates an variable with an empty value
    guesses = ''

    # determine the number of turns
    turns = 10

    # Create a while loop

    # check if the turns are more than zero
    while turns > 0:

        # make a counter that starts with zero
        failed = 0

        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:
                # print then out the character
                print(char),

            else:

                # if not found, print a dash
                print("_"),

                # and increase the failed counter with one
                failed += 1

        # if failed is equal to zero

        # print You Won
        if failed == 0:
            print("You won")
           # exit the script
            break

        # ask the user go guess a character
        guess = raw_input("guess a character:")

        print(guess)
        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        turns -= 1
        if guess in word:
            print("Correct")

        # if guess not in word:
        else:
            print(1)



            # print wrong
            print("Wrong")

            # how many turns are left


            # if the turns are equal to zero


        if turns == 0:
            # print "You Loose"
            print("You Lose")
            if playagain():
                playgame()
            return
        print("You have", + turns, 'more guesses')

playgame()