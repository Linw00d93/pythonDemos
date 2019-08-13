# -*- coding: utf-8 -*-
import random
import time




randomNumber = random.randint(1,20)
alive = True
print "Welcome to the Magic 8 ball"
print ("""    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
      .......""")
time.sleep(1)
while alive == True:
    print "Do you have a question for the Magic 8 ball?"
    raw = raw_input()
    userInput = raw.lower()
    if userInput == "yes" or userInput =='y':
        print "What is your question?"
        userQuestion = raw_input()
        print "Let me think about that"
        time.sleep(1)
        print "."
        time.sleep(2)
        print ".."
        time.sleep(3)
        print "..."
        if randomNumber == 1:
            print ("As I see it, yes.")

        elif randomNumber == 2:
            print ("Ask again later.")

        elif randomNumber == 3:
            print ("Better not tell you now.")

        elif randomNumber == 4:
            print ("Cannot predict now.")

        elif randomNumber == 5:
            print ("Concentrate and ask again.")

        elif randomNumber == 6:
            print ("Don’t count on it.")

        elif randomNumber == 7:
            print ("It is certain.")

        elif randomNumber == 8:
            print ("It is decidedly so.")

        elif randomNumber == 9:
            print ("Most likely.")

        elif randomNumber == 10:
            print ("My reply is no.")

        elif randomNumber == 11:
            print ("My sources say no.")

        elif randomNumber == 12:
            print ("Outlook not so good.")

        elif randomNumber == 13:
            print ("Outlook good.")

        elif randomNumber == 14:
            print ("Reply hazy, try again.")

        elif randomNumber == 15:
            print ("Signs point to yes.")

        elif randomNumber == 16:
            print ("Very doubtful.")

        elif randomNumber == 17:
            print ("Without a doubt.")

        elif randomNumber == 18:
            print ("Yes.")

        elif randomNumber == 19:
            print ("Yes – definitely.")

        elif randomNumber == 20:
            print ("You may rely on it.")

    elif userInput == "no" or userInput == "n":
        print "Bye then"
        exit()
    else:
        print "ERROR error Error"


#    ,dP9CGG88@b,
#  ,IP  _   Y888@@b,
# dIi  (_)   G8888@b
#dCII  (_)   G8888@@b
#GCCIi     ,GG8888@@@
#GGCCCCCCCGGG88888@@@
#GGGGCCCGGGG88888@@@@...
#Y8GGGGGG8888888@@@@P.....
# Y88888888888@@@@@P......
# `Y8888888@@@@@@@P'......
#    `@@@@@@@@@P'.......
#        """".......
