from random import randint
import time
while True:
    x = 0
    y = int(input('How many array\'s would you like created?'))
    while x < y:
        myList = [0, 0, 0]
        toChange = randint(0, 2)
        if toChange == 0:
            myList[0] = 1
        if toChange == 1:
            myList[1] = 1
        if toChange == 2:
            myList[2] = 1
        print(myList)
        x = x + 1
    
    
    
    
        
        
    
    
