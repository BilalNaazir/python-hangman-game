import random
from pip._vendor.distlib.compat import raw_input
import time

# welcoming the user

def playagain():
    choice = input('Play again? (y/n): ')

    return choice.lower() == 'y'
def playgame():
    name = raw_input("Please enter your name ")

    print("Hello, " + name, "Let's play play hangman!")

    print(" ")

    # wait for 1 second
    time.sleep(1)

    print("Fill in the blanks by entering a character")
    time.sleep(0.5)

    wordList=["secret", "kitchen", "great","distinguish","crave","feather","green","difficult","hard","believe","ravishing","pale","feeble","bounty" ]
    # the word is picked at random from the list
    word = random.choice(wordList)

    # variable created to hold each and every guess of the user as string
    guesses = ''

    # turns the user gets is equal to 3 + the  length of the word
    turns = len(word)+3

    # does the code if turns is more than 0
    while turns > 0:

        # make a counter that starts with zero
        numberOfFailTries = 0

        # iterates for every character in the word
        for char in word:

            # see if the character matches the players guess character
            if char in guesses:
                # print then out the character
                print(char),

            else:

                # if not found, print a dash
                print("_"),

                # and increase the failed counter with one
                numberOfFailTries += 1

        # if failed is equal to zero

        # print You Won
        if numberOfFailTries == 0:
            print("You won")
           # exit the script
            break

        # ask the user go guess a character
        guess = raw_input("guess a character:")

        # set the players guess to guesses
        guesses += guess


        if guess in word:
            print("Correct")
        # if guess not in word:
        else:

            turns -= 1
            # print wrong
            print("Wrong")


        # if the turns are equal to zero
        if turns == 0:
            # print "You Loose"
            print("You Lose")
            if playagain():
                playgame()
            return
        # how many turns are left
        print("You have", + turns, 'more guesses')

playgame()