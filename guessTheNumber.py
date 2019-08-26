import random
import os
import sys
from sys import stdin, __stdin__

randomNumber = 0
guessNumber = 0
randomNumber = random.randint(0,100)
guess = False


print(randomNumber)
while guess is False:
    print ("Guess a number: ")
    guessNumber = input()
    if randomNumber > guessNumber:
        print ("Number is too low, try again ")
    elif randomNumber < guessNumber:
        print ("Number is too high, try again ")
    elif randomNumber == guessNumber:
        txt = "You guessed correctly, the number is: {} "
        print (txt.format(randomNumber))
        guess = True
    else:
        print("ERROR ERROR ERROR")
print ("Thanks for playing")
