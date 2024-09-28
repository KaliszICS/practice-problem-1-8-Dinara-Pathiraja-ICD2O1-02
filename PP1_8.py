

def q1():
  bool1 = (True)
  bool2 = (False)
  print (bool1 and bool2)
  print (bool1 or bool2)

def q2():
  prompt = input('Enter an integer: ')
  integer1 = int(prompt)
  bool1 = True 
  bool1 = (integer1 != 0)
  bool2 = False 
  bool2 = (integer1 == 0)
  print (bool1 or bool2)

def q3():
  ask = input ("Enter a number: ")
  number1 = int (ask)
  bool1 = True 
  bool1 = (0 < number1 and 10 > number1)
  print (bool1)

def q4():
  food = input("Input food: ")
  drink = input ("Input drink: ")
  bool1 = False 
  bool1 = (food == "pizza" and drink == "pop")
  print(bool1 or not bool1)


def q5():
  ask = input("Enter an integer: ")
  integer1 = int(ask)
  bool1 = True 
  bool1 = (integer1 % 2 == 0)
  print (bool1 or not bool1)

#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
