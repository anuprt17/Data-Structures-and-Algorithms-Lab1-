#
# Author: Anupreet Kaur
# Student Number: 110313210
#
# Place the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Anupreet Kaur
# Student Number: 110313210
#

def wins_rock_scissors_paper( player, opponent):
	player1 = player.lower()
	opponent1 = opponent.lower()
	if( player1 == "rock" and opponent1 == "scissors")  :
		return True
	elif( player1 == "paper" and opponent1 == "rock"):
		return True
	elif( player1 == "scissors" and opponent1 == "paper"):
		return True	

	else :	
		return False    

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)	'''

def factorial(n):
    if isinstance(n, int) and n >= 0: 
        if n == 0: 
            return 1
        else:
            factorial = 1
            for i in range(1, n + 1): 
                factorial = factorial * i
            return factorial
    else: 
        return "Input is not valid......"  
               
    
''' Recursive Method
def fibonacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result
    '''


def fibonacci(n):   
    element1 = 0  
    element2 = 1  
    if n < 0:  
        print("please input 0 or greater")   
    elif n == 0:  
        return element1   
    elif n == 1:   
        return element2  
    else:
        for i in range(2, n + 1):   
            element3 = element1 + element2  
            element1 = element2   
            element2 = element3   
        return element2 

def sum_to_goal(list, goal):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == goal:
                return list[i] * list[j]
    return 0


class UpCounter:
    counter = 0
    def __init__( self, stepSize = 1):
        self.stepSize = stepSize 
    def count( self ):
        return self.counter
    def update( self ):
        self.counter += self.stepSize         
         

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.stepSize 
