#common coding questions
arrayText = [ 1,3,45,76,124,523,63,12,431,-3,64,7,39,9,23,12,21,43,65,79,98,72,5,9]
linwood = [None] * len(arrayText)

for i in range(0, len (arrayText)):
    linwood[i] = arrayText[i];


numberOfNumbers = len(arrayText)
print(numberOfNumbers)
print(arrayText.sort())
print(linwood.sort())
