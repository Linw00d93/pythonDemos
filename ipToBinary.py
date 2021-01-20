binary1=[]

print("Enter a IP address: ")

ipAddress = raw_input()

listOfBits = ipAddress.split(".")
numberOfBits = len(listOfBits)
def numberToBinary(num):
    if num <= 255 and numberOfBits == 4:
        if num >= 128:
            num = num - 128 
            binary1.append(1)
        else:
            binary1.append(0)

        if num >= 64:
            num = num - 64 
            binary1.append(1)
        else:
            binary1.append(0)

        if num >= 32:
            num = num - 32
            binary1.append(1)
        else:
            binary1.append(0)

        if num >= 16:
            num = num - 116
            binary1.append(1)
        else:
            binary1.append(0)

        if num >= 8:
            num = num - 8 
            binary1.append(1)
        else:
            binary1.append(0)

        if num >= 4:
            num = num - 4
            binary1.append(1)
        else:
            binary1.append(0)

        if num >= 2:
            num = num - 2 
            binary1.append(1)
        else:
            binary1.append(0)
    else:
        print("Invalid IP Address:" + ipAddress)
        exit()


    binary1.append('.')    
    return(binary1)

for x in listOfBits:
    num = int(x) 
    numberToBinary(num)

binary1.pop(len(binary1)-1)    
print ''.join(map(str, binary1))
 