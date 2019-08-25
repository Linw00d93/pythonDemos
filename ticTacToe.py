import random
import time
winConditionX = 'XXX'
winConditionO = 'OOO'
winCondition = False
userInput = 0
randomNumber = 0
dash = '|'
square1 = ' '
square2 = ' '
square3 = ' '
square4 = ' '
square5 = ' '
square6 = ' '
square7 = ' '
square8 = ' '
square9 = ' '

line1 = square1 + dash + square2 + dash + square3
lineBetween = '-----'
line2 = square4 + dash + square5 + dash + square6
line3 = square7 + dash + square8 + dash + square9
playing = True

win123 = ' '
win159 = ' '
win147 = ' '
win258 = ' '
win357 = ' '
win369 = ' '
win456 = ' '
win789 = ' '
"""
def function():
    if condition1:
        reaction1()
    elif condition2:
        reaction2()
    else:
        deafult_reaction()
        """



print ('Welcome to Tic Tac Toe, Your X and the AI is O')
userInput = raw_input('Would you like to play Tic Tac Toe: ')
if userInput == 'yes' or userInput == 'y':

    while playing == True:


        time.sleep(2)
        iconInput = input('What position would you like to put your icon; Options are 1-9 of the board: ')

        if iconInput == 1:
            if square1 == 'X' or square1 == 'O':
                print ('That square has already been used, try again')
            else:
                square1 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 2:
            if square2 == 'X' or square2 == 'O':
                print ('That square has already been used, try again')
            else:
                square2 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 3:
            if square3 == 'X' or square3 == 'O':
                print ('That square has already been used, try again')
            else:
                square3 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 4:
            if square4 == 'X' or square4 =='O':
                print ('That square has already been used, try again')
            else:
                square4 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 5:
            if square5 == 'X' or square5 == 'O':
                print ('That square has already been used, try again')
            else:
                square5 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 6:
            if square6 == 'X' or square6 == 'O':
                print ('That square has already been used, try again')
            else:
                square6 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 7:
            if square7 == 'X' or square7 == 'O':
                print ('That square has already been used, try again')
            else:
                square7 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 8:
            if square8 == 'X' or square8 == 'O':
                print ('That square has already been used, try again')
            else:
                square8 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif iconInput == 9:
            if square9 == 'X' or square9 == 'O':
                print ('That square has already been used, try again')
            else:
                square9 = 'X'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        else:
            print ('Error')

        win123 = square1 + square2 + square3
        win159 = square1 + square5 + square9
        win149 = square1 + square4 + square9
        win258 = square2 + square5 + square8
        win357 = square3 + square5 + square7
        win369 = square3 + square6 + square9
        win456 = square4 + square5 + square6
        win789 = square7 + square8 + square9
        if win123 == winConditionO:
            print ('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print ('Good bye')
            playing = False
            break
        elif win123 == winConditionX:
            print ('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print ('Good bye')
            playing = False
            break
        elif win159 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win159 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win147 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win147 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win258 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win258 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win357 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win357 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win369 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win369 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win456 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win456 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win789 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win789 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break

    #AI turn
        print('AI Turn: ')
        time.sleep(3)
        randomNumber = random.randint(1,9)
        if randomNumber == 1:
            if square1 == 'X' or square1 == 'O':
                print('That square has already been used, try again')
            else:
                square1 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 2:
            if square2 == 'X' or square2 == 'O':
                print('That square has already been used, try again')
            else:
                square2 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 3:
            if square3 == 'X' or square3 == 'O':
                print('That square has already been used, try again')
            else:
                square3 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 4:
            if square4 == 'X' or square4 =='O':
                print('That square has already been used, try again')
            else:
                square4 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 5:
            if square5 == 'X' or square5 == 'O':
                print('That square has already been used, try again')
            else:
                square5 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 6:
            if square6 == 'X' or square6 == 'O':
                print('That square has already been used, try again')
            else:
                square6 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 7:
            if square7 == 'X' or square7 == 'O':
                print('That square has already been used, try again')
            else:
                square7 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 8:
            if square8 == 'X' or square8 == 'O':
                print('That square has already been used, try again')
            else:
                square8 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        elif randomNumber == 9:
            if square9 == 'X' or square9 == 'O':
                print('That square has already been used, try again')
            else:
                square9 = 'O'
                print (square1 + dash + square2 + dash + square3)
                print (lineBetween)
                print (square4 + dash + square5 + dash + square6)
                print (lineBetween)
                print (square7 + dash + square8 + dash + square9)
        else:
            print('Error')

        win123 = square1 + square2 + square3
        win159 = square1 + square5 + square9
        win149 = square1 + square4 + square9
        win258 = square2 + square5 + square8
        win357 = square3 + square5 + square7
        win369 = square3 + square6 + square9
        win456 = square4 + square5 + square6
        win789 = square7 + square8 + square9
        if win123 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win123 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win159 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win159 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win147 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win147 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win258 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win258 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win357 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win357 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win369 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win369 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win456 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win456 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win789 == winConditionO:
            print('The AI Won')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break
        elif win789 == winConditionX:
            print('You beat the AI')
            print (square1 + dash + square2 + dash + square3)
            print (lineBetween)
            print (square4 + dash + square5 + dash + square6)
            print (lineBetween)
            print (square7 + dash + square8 + dash + square9)
            print('Good bye')
            playing = False
            break


elif userInput =='no' or userInput == 'n':
    print('Good bye')
    playing = False
    SystemExit()
else:
    print('Error')
