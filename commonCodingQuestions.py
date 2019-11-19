#common coding questions
#import copy
#import numpy
arrayText = [ 1,3,45,76,124,523,63,12,431,-9,67,34,124,768,97,65,423,135,876,96,99,22,4,55,64,7,39,9,23,12,21,43,65,79,98,72,5,9]


"""
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
"""

"""
#Daily Coding Problem: Problem #1
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
x = 0
y = 0
numberFound = False
while numberFound == False:
    print("Please Enter Number to find the total for:")
    num1 = input()
    print num1
    for i in range(len(arrayText)):
        if (arrayText[y] + arrayText[x] == num1):
            print " YOU FOUND IT:"
            print(arrayText[y])
            print(arrayText[x])
            exit()
            numberFound == True
        else:
            print "Next"
        x = x+1
    x = 0
    y = y + 1
"""

"""
#Daily Coding Problem: Problem #2
#Given an array of integers, return a new array such that each element at
#index i of the new array is the product of all the numbers in the original array except the one at i.
arrayText1 = [6,7,8,9]
product = 1
num2 = 0
arraysample =[]
placeholder = 0
placeholder1 = 0
Long = len(arrayText1)
long1 = Long -1
print arrayText1
for items in range(long1):
    num2 = arrayText1.pop(items)
    placeholder = arrayText1[items]
    for x in range(long1):
        placeholder1 = arrayText1[x]
        product =  product * placeholder1
    arraysample.append(product)
    product = 1
    arrayText1 = [6,7,8,9]


arrayText1.pop(long1)
placeholder = arrayText[0]
for x in range(long1):
    placeholder1 = arrayText1[x]
    product =  product * placeholder1
arraysample.append(product)
print (arraysample)
"""
"""
#Daily Coding Problem: Problem #4
#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
#find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

givenArray = [1, 2, 0,5,3,6,3,6,2]
scale = 10
checkingArray = []
lengthCheck = len(givenArray)
min1 = -1
testArray = givenArray

while min1 < 0:
    min1 = min(testArray)
    testArray.remove(min1)

for x in range(min1,scale):
    checkingArray.append(x)

testArray.append(min1)

for x in range(min1,scale):
    if x in testArray:
        print("")
    else:
        print ("the number missing is: ")
        print (x)
        print(givenArray)
        exit()
"""
