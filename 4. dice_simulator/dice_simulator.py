import random   # use random library for generating random number
import time     # use time library for time delay 

min_val = 1     # minimum value of dice
max_val = 6     # maximum value of dice

roll_again = 'yes'
#
# loop for roll the dice
#
while (roll_again == 'yes' or roll_again == 'y'):
    print('Rolling the Dice...')
    #
    # 1 sec time delay
    #
    time.sleep(1)  
    print('The value is ...')
    time.sleep(1)
    #
    # print the random number from 1 to 6 for dice
    #
    print(random.randint(min_val, max_val)) 
    #
    # ask for roll the dice
    #
    roll_again = input('Roll the Dice again ?\n')