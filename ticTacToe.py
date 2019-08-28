import random
import time
winConditionX = 'XXX'
winConditionO = 'OOO'
winCondition = False
iconNotPlace = False
userInput = 0
randomNumber = 0
global playing
playing = True
lineBetween = '-----'
dash = '|'
square1, square2, square3, square4, square5, square6, square7, square8, square9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

line1 = square1 + dash + square2 + dash + square3
line2 = square4 + dash + square5 + dash + square6
line3 = square7 + dash + square8 + dash + square9

win123, win159, win147, win258, win357, win369, win456, win789 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '


#Print the board function--------------------------------
def print_The_Board ():
    print (square1 + dash + square2 + dash + square3)
    print (lineBetween)
    print (square4 + dash + square5 + dash + square6)
    print (lineBetween)
    print (square7 + dash + square8 + dash + square9)
#check for winner function---------------------------------------------------
def check_For_Winner():
    global winner
    winner = 0
    win123 = square1 + square2 + square3
    win159 = square1 + square5 + square9
    win149 = square1 + square4 + square9
    win258 = square2 + square5 + square8
    win357 = square3 + square5 + square7
    win369 = square3 + square6 + square9
    win456 = square4 + square5 + square6
    win789 = square7 + square8 + square9
    if win123 == winConditionO or win159 == winConditionO or win149 == winConditionO or win258 == winConditionO or win357 == winConditionO or win369 == winConditionO or win456 == winConditionO or win789 == winConditionO:
        print('The AI Won')
        print_The_Board()
        print('Good bye')
        winner += 1
        return winner
    elif win123 == winConditionX or win159 == winConditionX or win149 == winConditionX or win258 == winConditionX or win357 == winConditionX or win369 == winConditionX or win456 == winConditionX or win789 == winConditionX:
        print('You beat the AI ')
        print_The_Board()
        print('Good bye ')
        winner += 1
        return winner

#check for cat eyes function-------------------------------------------------------------------------------------------------
def check_If_Cat_Eyes():
    global tie
    tie = 0
    line1 = square1 + square2 + square3
    line2 = square4 + square5 + square6
    line3 = square7 + square8 + square9
    if ' ' in line1 or ' ' in line2 or ' ' in line3:
        print(' ')
        return tie
    else:
        print('Cats Eyes ')
        print_The_Board()
        print('Game over, good bye ')
        tie += 1
        return tie





print ('Welcome to Tic Tac Toe, Your X and the AI is O ')
userInput = raw_input('Would you like to play Tic Tac Toe (options; yes or no): ')
userInput.lower()
if userInput == 'yes' or userInput == 'y':

    while playing == True:

        iconNotPlace = False
        while iconNotPlace == False:
#User Turn-----------------------------------------------------------------------------------------------------
            iconInput = input('What position would you like to put your icon; Options are 1-9 of the board: ')

            if iconInput == 1:
                if square1 == 'X' or square1 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square1 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 2:
                if square2 == 'X' or square2 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square2 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 3:
                if square3 == 'X' or square3 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square3 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 4:
                if square4 == 'X' or square4 =='O':
                    print ('That square has already been used, try again')
                else:
                    square4 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 5:
                if square5 == 'X' or square5 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square5 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 6:
                if square6 == 'X' or square6 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square6 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 7:
                if square7 == 'X' or square7 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square7 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 8:
                if square8 == 'X' or square8 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square8 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            elif iconInput == 9:
                if square9 == 'X' or square9 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square9 = 'X'
                    iconNotPlace = True
                    print_The_Board()
            else:
                print ('Error')

#Check for winner after user turn---------------------------------------------------------------------
        check_For_Winner()
        if winner == 1:
            playing = False
            break
#Check for cat eyes after user turn-----------------------------------------------------------------------------------
        check_If_Cat_Eyes()
        if tie == 1:
            playing = False
            break

#AI turn-------------------------------------------------------
        print('AI Turn: ')
        time.sleep(3)
        iconNotPlace = False
        while iconNotPlace == False:
            randomNumber = random.randint(1,9)
            if randomNumber == 1:
                if square1 == 'X' or square1 == 'O':
                    continue
                else:
                    square1 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 2:
                if square2 == 'X' or square2 == 'O':
                    continue
                else:
                    square2 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 3:
                if square3 == 'X' or square3 == 'O':
                    continue
                else:
                    square3 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 4:
                if square4 == 'X' or square4 =='O':
                    continue
                else:
                    square4 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 5:
                if square5 == 'X' or square5 == 'O':
                    continue
                else:
                    square5 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 6:
                if square6 == 'X' or square6 == 'O':
                    continue
                else:
                    square6 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 7:
                if square7 == 'X' or square7 == 'O':
                    continue
                else:
                    square7 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 8:
                if square8 == 'X' or square8 == 'O':
                    continue
                else:
                    square8 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            elif randomNumber == 9:
                if square9 == 'X' or square9 == 'O':
                    continue
                else:
                    square9 = 'O'
                    iconNotPlace = True
                    print_The_Board()
            else:
                print('Error')

#check for winnder after AI turn---------------------------------------------------------------
        check_For_Winner()
        if winner == 1:
            playing = False
            break
#check for cat eyes after AI turn-----------------------------------------------------------------
        check_If_Cat_Eyes()
        if tie == 1:
            playing = False
            break

elif userInput =='no' or userInput == 'n':
    print('Good bye')
    playing = False
    SystemExit()
else:
    print('Error')
