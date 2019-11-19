#stadomcountlist

#sort list by lowest number
#count from lowest number
#and compare to standarom list
#when compare fails that is the magic number
import random
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
