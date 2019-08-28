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

dash = '|'
square1, square2, square3, square4, square5, square6, square7, square8, square9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '

line1 = square1 + dash + square2 + dash + square3
lineBetween = '-----'
line2 = square4 + dash + square5 + dash + square6
line3 = square7 + dash + square8 + dash + square9

win123, win159, win147, win258, win357, win369, win456, win789 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '


def printTheBoard ():
    print (square1 + dash + square2 + dash + square3)
    print (lineBetween)
    print (square4 + dash + square5 + dash + square6)
    print (lineBetween)
    print (square7 + dash + square8 + dash + square9)
def checkForWinner(playing):
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
        printTheBoard()
        print('Good bye')
        playing = False
        return playing
        print(playing)
        SystemExit()
    elif win123 == winConditionX or win159 == winConditionX or win149 == winConditionX or win258 == winConditionX or win357 == winConditionX or win369 == winConditionX or win456 == winConditionX or win789 == winConditionX:
        print('You beat the AI')
        printTheBoard()
        print('Good bye')
        playing = False
        return playing
        SystemExit()




print ('Welcome to Tic Tac Toe, Your X and the AI is O')
userInput = raw_input('Would you like to play Tic Tac Toe: ')
if userInput == 'yes' or userInput == 'y':

    while playing == True:

        iconNotPlace = False
        while iconNotPlace == False:

            iconInput = input('What position would you like to put your icon; Options are 1-9 of the board: ')

            if iconInput == 1:
                if square1 == 'X' or square1 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square1 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 2:
                if square2 == 'X' or square2 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square2 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 3:
                if square3 == 'X' or square3 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square3 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 4:
                if square4 == 'X' or square4 =='O':
                    print ('That square has already been used, try again')
                else:
                    square4 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 5:
                if square5 == 'X' or square5 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square5 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 6:
                if square6 == 'X' or square6 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square6 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 7:
                if square7 == 'X' or square7 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square7 = 'X'
                    iconNotPlace = True
                    printTheBoard()
                if square8 == 'X' or square8 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square8 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            elif iconInput == 9:
                if square9 == 'X' or square9 == 'O':
                    print ('That square has already been used, try again')
                else:
                    square9 = 'X'
                    iconNotPlace = True
                    printTheBoard()
            else:
                print ('Error')

        checkForWinner(playing)
        print(playing)

    #AI turn
        print('AI Turn: ')
        time.sleep(3)
        iconNotPlace = False
        randomNumber = random.randint(1,9)
        while iconNotPlace == False:
            if randomNumber == 1:
                if square1 == 'X' or square1 == 'O':
                    break
                else:
                    square1 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 2:
                if square2 == 'X' or square2 == 'O':
                    break
                else:
                    square2 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 3:
                if square3 == 'X' or square3 == 'O':
                    break
                else:
                    square3 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 4:
                if square4 == 'X' or square4 =='O':
                    break
                else:
                    square4 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 5:
                if square5 == 'X' or square5 == 'O':
                    break
                else:
                    square5 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 6:
                if square6 == 'X' or square6 == 'O':
                    break
                else:
                    square6 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 7:
                if square7 == 'X' or square7 == 'O':
                    break
                else:
                    square7 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 8:
                if square8 == 'X' or square8 == 'O':
                    break
                else:
                    square8 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            elif randomNumber == 9:
                if square9 == 'X' or square9 == 'O':
                    break
                else:
                    square9 = 'O'
                    iconNotPlace = True
                    printTheBoard()
            else:
                print('Error')

        checkForWinner(playing)
        print(playing)

elif userInput =='no' or userInput == 'n':
    print('Good bye')
    playing = False
    SystemExit()
else:
    print('Error')
