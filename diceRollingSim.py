import random
dice1 = 0
dice2 = 0
diceTotal = 0
startMoney = 1000
stillPlaying = True
currentMoney = startMoney
currentBet = 0
chance = 0

while stillPlaying == True:

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    userInput = raw_input("Would you you like to roll dice  ")
    if userInput == 'yes' or userInput == 'y':

        userInput = raw_input("Would you like to bet some money ")
        if userInput == 'yes' or userInput == 'y':

            amountToBet = input('How much would you like to bet ')
            if amountToBet <= currentMoney:

                diceTotal = dice1 + dice2
                if diceTotal == 7 or diceTotal == 11:

                    print("You Win")
                    currentMoney = currentMoney + amountToBet
                    txt1 = "Dice 1 is: {} "
                    txt2 = "Dice 2 is: {} "
                    txt3 = "Current Money: {} "

                    print (txt1.format(dice1))
                    print (txt2.format(dice2))
                    print (txt3.format(currentMoney))
                elif diceTotal == 2 or diceTotal == 3 or diceTotal == 12:

                    print('Craps; you lose')
                    currentMoney = currentMoney - amountToBet
                    txt1 = "Dice 1 is: {} "
                    txt2 = "Dice 2 is: {} "
                    txt3 = "Current Money: {} "

                    print (txt1.format(dice1))
                    print (txt2.format(dice2))
                    print (txt3.format(currentMoney))
                else:

                    chance = random.randint(1,100)
                    if chance > 50:

                        print("Point, you Win")
                        currentMoney = currentMoney + amountToBet
                        txt2 = "Dice 2 is: {} "
                        txt3 = "Current Money: {} "

                        print (txt1.format(dice1))
                        print (txt2.format(dice2))
                        print (txt3.format(currentMoney))
                    else:

                        print('Point; you lose')
                        currentMoney = currentMoney - amountToBet
                        txt1 = "Dice 1 is: {} "
                        txt2 = "Dice 2 is: {} "
                        txt3 = "Current Money: {} "
                        print (txt1.format(dice1))
                        print (txt2.format(dice2))
                        print (txt3.format(currentMoney))


            elif amountToBet > currentMoney:

                print('Error you dont have enough money')
                txt4 = "The current amount: {}"
                print(txt4.format(currentMoney))
            else:

                print('Error')
        else:

            print('Maybe next round')
            txt1 = "Dice 1 is: {} "
            txt2 = "Dice 2 is: {} "
            print (txt1.format(dice1))
            print (txt2.format(dice2))
    else:

        print("Thanks for coming")
        stillPlaying = False
        SystemExit()
