#calcualtor
def addition():
	print("Please Enter Number 1:")
        num1 = input()
        print("Please Enter Number 2:")
        num2 = input()
	total = num1 + num2
	print 'The sum is: ',total
def subtract():
 	print("Please Enter Number 1:")
        num1 = input()
        print("Please Enter Number 2:")
        num2 =input()
        total = num1 - num2
	print 'The total: ',total
def multiplication():
	print("Please Enter Number 1:")
        num1 = input()
        print("Please Enter Number 2:")
        num2 = input()
        product = num1 * num2
	print 'The product is: ' ,product
def divison():
	print("Please Enter Number 1:")
        num1 =input()
        print("Please Enter Number 2:")
        num2 =input()
	if num2 == 0:
            print("Error")
        else:
            quotient = num1 / num2
	    print 'The quotient is: ', quotient


print('Would you like to do some math: ')
sm = raw_input()

if (sm == 'yes' or sm == 'y'):
    print("Please enter your name: ")
    name = raw_input()
    print ("Hello," ,name)
    try:
        while True:
            print("What kind of math would you like to do")
            print("To exit Ctrl+C")
            print(" + Addition - Subject * Multiplcation / Division")
            operation = raw_input()
            if (operation == "+"):
               	addition()
            elif (operation == "-"):
             	subtraction()
            elif (operation == "*"):
              	multiplication()
            elif (operation == "/"):
		divison()    
            else:
                print("Error")
                break
    except (KeyboardInterrupt, SystemExit):
            pass
elif (sm == 'no' or sm == 'n'):
    print("Bye")
else:
    print('Error')
