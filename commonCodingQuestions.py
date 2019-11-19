#common coding questions
import copy
import numpy
arrayText = [ 1,3,45,76,124,523,63,12,431,-9,67,34,124,768,97,65,423,135,876,96,99,22,4,55,64,7,39,9,23,12,21,43,65,79,98,72,5,9]
"""x = 0
y = 0
numberFound = False

#Palindrome
def split(word):
    return list(word)

wordtext = 'racecar'

wordList = split(wordtext)
backWardsWord = (list(reversed(wordList)))

if wordList == backWardsWord:
    txt = wordtext + ' is a Palindrome'
    print (txt)
else:
    txt1 = wordtext + ' is not a Palindrome'
    print (txt1)


while numberFound == False:

    for i in range(len(arrayText)):

        if (arrayText[y] + arrayText[x] == 0):
            print " YOU FOUND IT:"
            print(arrayText[y])
            print(arrayText[x])
            exit()
        else:
            print "Next"
        x = x+1
    x = 0
    y = y + 1
"""

arrayText1 = [1,2,3,4]
product =1
num2 = 0
Long = len(arrayText1)
for items in range(Long):
    num2 = arrayText1.pop(items)
    print ("arrayText")
    print(arrayText1)
    print("num2")
    print (num2)
    #arrayText.insert(items,num2)
    #print (arrayText)
    for x in range(Long):

    arrayText.insert(items,num2)
    print (arrayText1)
