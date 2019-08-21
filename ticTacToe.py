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
print line1
print lineBetween
print line2
print lineBetween
print line3
playing = True



while playing == True:

    userInput = raw_input('Would you like to play Tic Tac Toe ')
    if userInput == 'yes' or userInput == 'y':
        iconInput = input('What Position would you like to put your icon')
        if iconInput == 1:
            if square1 == 'X' or square1 == 'O':
                print'That square has already been used, try again'
            else:
                square1 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 2:
                if square2 == 'X' or square2 == 'O':
                    print'That square has already been used, try again'
                else:
                    square2 = 'X'
                    print square1 + dash + square2 + dash + square3
                    print lineBetween
                    print square4 + dash + square5 + dash + square6
                    print lineBetween
                    print square7 + dash + square8 + dash + square9
        elif iconInput == 3:
            if square3 == 'X' or square3 == 'O':
                print'That square has already been used, try again'
            else:
                square3 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 4:
            if square4 == 'X' or square4 =='O':
                print'That square has already been used, try again'
            else:
                square4 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 5:
            if square5 == 'X' or square5 == 'O':
                print'That square has already been used, try again'
            else:
                square5 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 6:
            if square6 == 'X' or square6 == 'O':
                print'That square has already been used, try again'
            else:
                square6 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 7:
            if square7 == 'X' or square7 == 'O':
                print'That square has already been used, try again'
            else:
                square7 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 8:
            if square8 == 'X' or square8 == 'O':
                print'That square has already been used, try again'
            else:
                square8 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        elif iconInput == 9:
            if square9 == 'X' or square9 == 'O':
                print'That square has already been used, try again'
            else:
                square9 = 'X'
                print square1 + dash + square2 + dash + square3
                print lineBetween
                print square4 + dash + square5 + dash + square6
                print lineBetween
                print square7 + dash + square8 + dash + square9
        else:
            print'Error'
    elif userInput =='no' or userInput == 'n':
        print'Good bye'
        playing = False
        SystemExit()
else:
    print 'Error'





"""
if userInput = 1
elif userInput = 2
elif userInput = 3
elif
elif
elif
elif
elif
elif
else
"""
