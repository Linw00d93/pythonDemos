import random
import time




randomNumber = random.randint(0,25)
List = ["export", "fabric", "junior", "letter", "matter", "narrow", "normal", "public", "reward", "sexual", "animal", "arrive", "common", "copper", "doctor", "dollar", "assess", "system", "depend", "demand", "dinner", "theory", "united", "worker", "button", "yellow"]
guessLetter = ["_","_","_","_","_","_"]
playing = True
guessCount = 15
hangManWord = List[randomNumber]
hmwList = list(hangManWord)
#print(hangManWord)
#used for testing.
#print(hmwList)




print("Welcome to HangMan your word has six letters")
print("and you have 10 guesses to guess the word")
time.sleep(1)
while guessCount != 0:
    print("Would you like to guess the word or guess a letter")
    print("Type word for word guess or letter for letter guess")
    raw = raw_input()
    userInput = raw.lower()
    print (userInput)

    if userInput == "word":
        print("Please enter your guess")
        userInputWord = raw_input()
        if userInputWord == hangManWord:
            print("You guess the word correctly !!!")
            print("The word was:" )
            print(hangManWord)
            print("The number of guess left:")
            print(guessCount)
            print("Great Game !!")
            exit()
        else:
            print("Sorry that is not the word")
            guessCount= guessCount - 1
            print(guessCount)
            break
    elif userInput =="letter":
        print(guessLetter)
        print("Please enter your letter guess")
        userInputLetter=raw_input()
        letterGuessed = hangManWord.find(userInputLetter)
        if letterGuessed > -1:
            print("Your letter was found in the word")
            if hmwList == 0:
                guessLetter[0] = userInputLetter
                del hmwList[0]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 1:
                guessLetter[1] = userInputLetter
                del hmwList[1]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 2:
                guessLetter[2] = userInputLetter
                del hmwList[2]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 3:
                guessLetter[3] = userInputLetter
                del hmwList[3]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 4:
                guessLetter[4] = userInputLetter
                del hmwList[4]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 5:
                guessLetter[5] = userInputLetter
                del hmwList[5]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
            elif letterGuessed == 6:
                guessLetter[6] = userInputLetter
                del hmwList[6]
                guessCount = guessCount - 1
                print("Guess Count:")
                print(guessCount)
                print(guessLetter)
        else:
            print("the letter is not found within the word")
            guessCount = guessCount - 1
            print(guessCount)
            break
    else:
        print(" ERROR ERROR ERROR")
