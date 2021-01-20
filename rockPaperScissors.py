import random
import os
import sys
from sys import stdin, __stdin__
playing = True


while playing == True:
    randomNumber = 0
    randomNumber = random.randint(1,3)
    #print(randomNumber)

    if randomNumber == 1:
        computer = 'rock' 
    elif randomNumber == 2:
        computer = 'paper'
    else:
        computer = 'scissors'

    print("Rock Paper or Scissor")
    print("Your choice: ")
    userInput = raw_input()
    userInput.lower()
    """
    rock beats scissor
    scissor beats paper 
    paper beats rock
    """ 
    if userInput == computer:
        print("Tie Computer: " + computer + " vs User:" + userInput)
    elif userInput == "rock" and computer == "scissors":
        print(" You won User: " + userInput + " vs Computer: " + computer)
    elif userInput == " scissors" and computer == "paper":
        print(" You won User: " + userInput + " vs Computer: " + computer)
    elif userInput == "paper" and computer == "rock":
        print(" You won User: " + userInput + " vs Computer: " + computer)
    else:
        print("You lost Computer: " + computer + " vs User: " + userInput)

    print("Would you like to play again, Y/N: ")
    stillPlaying = raw_input()
    stillPlaying.lower
    if stillPlaying == 'y':
        playing == True
    elif stillPlaying == 'n':
        exit()
    else:
        print("Error")
