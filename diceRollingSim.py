import random
dice1 = 0
dice2 = 0

stillPlaying = True

while stillPlaying is True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    userInput = raw_input("Would you you like to roll dice  ")
    if userInput == 'yes' or userInput == 'y':
        txt1 = "Dice 1 is: {} "
        txt2 = "Dice 2 is: {} "
        print (txt1.format(dice1))
        print (txt2.format(dice2))
    else:
        print("Thanks for coming")
        stillPlaying =False
