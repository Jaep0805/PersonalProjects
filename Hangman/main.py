
def play():
    correct = False
    counter = -1
    print("Time to play hangman!")
    while(correct == False):
        word = input('Which word should we guess? : ' )
        confirm = input("Is " + word + " correct? (answer 'yes' or 'no') : ")
        if(confirm == 'yes'):
            correct = True

    wordlength = len(word)
    print("Time to guess! ")
    print("The word is " + str(wordlength) + ' characters long')
    wordlist = list(word)
    guesswordlist = list()
    for i in range(0, wordlength):
        guesswordlist.append('-')
    for i in guesswordlist:
        print(i, end = ' ')
    print(' ')

    while doescontain(guesswordlist) and counter < 10:
        counter = counter + 1
        print ("guess counter = " + str(counter))
        guess(wordlist, guesswordlist)


    if counter > 9 :
        print("LOSE")
        print("You have guessed over 10 times")
    elif not (doescontain(guesswordlist)):
        print("WIN")
        print("You won in " + str(counter) + ' guesses')


def doescontain(wlist):
    for val in wlist:
        if val == '-':
            return True
        else: 
            continue
    return False

def guess(wordlist, guesswordlist):
    guessletter = input("What is your guess : ")
    copylist = guesswordlist.copy()
    guesswordlist.clear()
    if(guessletter in wordlist):
        print('correct letter!')
        for char in wordlist:
            if char == guessletter:
                guesswordlist.append(guessletter)
            elif copylist[wordlist.index(char)] != '-':
                guesswordlist.append(copylist[wordlist.index(char)])
            else:
                guesswordlist.append('-')
    else :
        print("wrong letter")
        for thing in copylist:
            guesswordlist.append(thing)

    for i in guesswordlist:
        print(i, end = ' ')
    print(' ')


play()