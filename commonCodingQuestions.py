#common coding questions
import copy
import os
#import numpy
import random
arrayText = [ 1,3,45,76,124,523,63,12,431,-9,67,34,124,768,97,65,423,135,876,96,99,22,4,55,64,7,39,9,23,12,21,43,65,79,98,72,5,9]

"""
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = raw_input()
    alphaN = False
    alpha = False
    digits = False
    lowerC = False
    upperC = False
    for x in s: 
        if (x.isalnum()) == True: 
            alphaN = True
        if (x.isalpha()) == True: 
            alpha = True
        if (x.isdigit()) == True: 
            digits = True
        if (x.islower()) == True: 
            lowerC = True
        if (x.isupper()) == True: 
            upperC = True

print alphaN
print alpha 
print digits
print lowerC
print upperC 

In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    total = 0
    subLen = len(sub_string)
    strLen = len(string)
    for x in range((strLen-subLen)+1):
        answer = string.find(sub_string,x,x + subLen)
        if answer > -1:
            total = total + 1
    return total

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count


Print the name(s) of any student(s) having the second lowest grade in Physics; 
if there are multiple students, order their names alphabetically 
and print each one on a new line.

studentNameList=[]
studentScoreList=[]
for x in range(int(raw_input())):
    
    name = raw_input()
    studentNameList.append(name)
    score = float(raw_input())
    studentScoreList.append(score)

runnerUpListScore =[] 
runnerUpListName = []
maxScore =min(studentScoreList)
numberToPop = studentScoreList.index(maxScore)

i = 0

while i < len(studentScoreList):

    if studentScoreList[i] > maxScore: 
        runnerUpListScore.append(studentScoreList[i])
        runnerUpListName.append(studentNameList[i])  
    i = i + 1


runnerUpScore = min(runnerUpListScore)
runnerUpIndex = runnerUpListScore.index(runnerUpScore)

answer= []

for i in range(len(runnerUpListScore)):
     if runnerUpListScore[i] == runnerUpScore: 
         answer.append(runnerUpListName[i])
answer.sort()
for i in range(len(answer)):
    print answer[i]

Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.

n=input()
a=map(int,input().split())
a=list(set(a))
a.remove(max(a))
print (max(a))



You are given the year, and you have to write a function to check if the year is leap or not.
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    leap = False
    
    if year % 4 == 0 and not(year % 100 == 0):
        leap = True
    elif year % 4 == 0 and year % 100 ==0 and year % 400 == 0:
        leap = True
    else:
        leap = False

    
    return leap

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
"""
#Daily Coding Problem 7
#Given the mapping a = 1, b = 2, ... z = 26,
#and an encoded message, count the number of ways it can be decoded.

inputArray = []
linwood = 0
inputArrayFirstHalf = []
inputArraySecondHalf = []
output = []
output1 = []
output2 = []
numberOne = 0
numberTwo = 0
placeHolder = 0
x = 0
Decode = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
randomNumber = random.randint(1,9)
inputArray.append(randomNumber)
randomNumber = random.randint(1,9)
inputArray.append(randomNumber)
randomNumber = random.randint(1,9)
inputArray.append(randomNumber)
print(inputArray)

inputArrayFirstHalf = inputArray.copy()

numberOne = inputArrayFirstHalf.pop(0)
numberTwo = inputArrayFirstHalf.pop(0)
numberOne_int = int(numberOne)
numberTwo_int = int(numberTwo)
placeHolder = numberOne_int + numberTwo_int
inputArrayFirstHalf.insert(0,placeHolder)


inputArraySecondHalf = inputArray.copy()
numberTwo = inputArraySecondHalf.pop(2)
numberOne = inputArraySecondHalf.pop(1)
numberOne_int = int(numberOne)
numberTwo_int = int(numberTwo)
placeHolder = numberOne_int + numberTwo_int
inputArraySecondHalf.insert(1,placeHolder)


print(inputArray)
print(inputArrayFirstHalf)
print(inputArraySecondHalf)
for l in inputArray:
 x = inputArray[linwood]
 x_int = int(x)
 letter = Decode[x_int]
 output.append(letter)
 linwood = linwood + 1

linwood = 0

for l in inputArrayFirstHalf:
  x = inputArrayFirstHalf[linwood]
  x_int = int(x)
  letter = Decode[x_int]
  output1.append(letter)
  linwood = linwood + 1

linwood = 0

for l in inputArraySecondHalf:
  x = inputArraySecondHalf[linwood]
  x_int = int(x)
  letter = Decode[x_int]
  output2.append(letter)
  linwood = linwood + 1

print(output)
print(output1)
print(output2)
"""

#Daily Coding Problem: 11
#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
#return all strings in the set that have s as a prefix.

dict = open('./pythonDemos/words.txt' , 'r')
print(dict)

#Daily Coding Problem 12
#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
#Given N, write a function that returns the number of unique ways you can climb the staircase.
#The order of the steps matters.

#Daily Coding problem 22
#Given a dictionary of words and a string made up of those words (no spaces),
#return the original sentence in a list. If there is more than one possible reconstruction,
#return any of them. If there is no possible reconstruction, then return null.

#Daily Coding problem 27
#Given a string of round, curly, and square open and closing brackets,
#return whether the brackets are balanced (well-formed).

def mergeFiles(fileSizes):
    totalTime = 0
    size = len(fileSizes) 
    fileSizes.sort()
    finalTotal = 0 
    while size > 1:
        num1 = fileSizes[0]
        num2 = fileSizes[1]
        totalTime = num1 + num2
        fileSizes.pop(0)
        fileSizes.pop(0)        
        fileSizes.insert(0,totalTime)
        fileSizes.sort()
        size = size - 1 
        finalTotal = finalTotal + totalTime
    return(finalTotal)
