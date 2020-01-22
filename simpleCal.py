#!/usr/bin/env python2.7
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








print('Would you like to do some math: ')
sm = raw_input()

if (sm == 'yes' or sm == 'y'):
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
              	print("Please Enter Number 1:")
                num1 = input()
                print("Please Enter Number 2:")
                num2 = input()
                product = num1 * num2
            	print 'The product is: ' ,product
            elif (operation == "/"):
                print("Please Enter Number 1:")
                num1 =input()
                print("Please Enter Number 2:")
                num2 =input()
            	if num2 == 0:
                    print("Error")
                else:
                    quotient = num1 / num2
                    print "The quotient is:", quotient
            else:
                print "Error"
                break
    except (KeyboardInterrupt, SystemExit):
            pass

elif (sm == 'no' or sm == 'n'):
    print("Bye")
else:
    print('Error')
