import math

for i in range(1,1001):
  foo = i%3
  bar = i%5
  #print foo
  #print bar
  if (foo == 0 and bar == 0):
      print "FizzBuzz"
  elif (bar == 0):
      print "Buzz"
  elif (foo == 0):
    print "Fizz"
  else:
    print i
