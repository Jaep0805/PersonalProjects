
import random
from dice import Dice


def play():
    #ask user for number of die, and number of rolls
    dicenumber = int(input("How many dices would you like to roll? : "))
    times = int(input("How many times would you like to roll? : "))

    #create list to store all dice
    die = [Dice()] * dicenumber
    
    #create list to store all result values
    results = [0] * dicenumber * 6
    result = 0
    print(' ', end = '')

    #roll the die and store values in results array
    for i in range(0,times):
        for l in die:
            result += l.roll()
        results[result -1] = results[result -1] +1
        result = 0

    #print out the frequency table
    print("Frequency : ")
    for j in range(1 * dicenumber,dicenumber *6+1):
        print(str(j), end = ': ')
        print(results[j-1])
    print(' ')

    #print out the percentage table
    print('Percentage : ')
    for k in range(1 * dicenumber,dicenumber * 6 + 1):
        print(str(k) + ': ' + str(round(results[k-1]/times  * 100, 2)) + '%')


    #ask user if they want to play again, if yes, recursion
    playagain = input("Would you like to play again? : (yes/no)")
    if playagain == 'yes':
        play()
    else :
        ''


#run the function
play()

