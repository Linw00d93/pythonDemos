arrayText = [99,78,3,45,76,124,37,523,63,12,431,9,67,34,124,768,97,65,423,135,876,96,99,22,4,55,64,7,39,9,23,12,21,43,65,79,98,72,5,9]

#high low pivot
i = 0
j = len(arrayText)
j = j - 1
arrayText1 = []
arrayText2 = []
arrayText1 = arrayText.sort()
print(arrayText1)
print(len(arrayText))
print (j)
print(arrayText[i])
print(arrayText[j])

for k in range(len(arrayText)):
    if i > j:
        print(i)
        print(j)
        j = j - 1
        i = i + 1
    elif j > i:
        print(arrayText)
        j = j - 1
        i = i + 1
