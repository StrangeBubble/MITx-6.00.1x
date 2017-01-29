# Problem 4 - The Game

# (15/15 points)
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an
# interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions,
# isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# Hints:
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a
# random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When
# you enter in your solution in the tutor, you only need to give your hangman function.

# Consider using lower() to convert user input to lower case. For example:
# guess = 'A'
# guessInLowerCase = guess.lower()
# Consider writing additional helper functions if you need them!

# There are four important pieces of information you may wish to store:
# secretWord: The word to guess.
# lettersGuessed: The letters that have been guessed so far.
# mistakesMade: The number of incorrect guesses made so far.
# availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed
# from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've
# already guessed that - so try again!).

# Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to
# paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the
# problem. If you use additional helper functions, you will need to paste those definitions here.

# Your function should include calls to input to get the user's guess.


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # set guessLeft to 8 (the number of guesses the player gets)
    guessLeft = 8
    
    # create a list to store lettersGuessed
    lettersGuessed = [ ]
    
    # find the length of the secretWord
    k = len(secretWord)
    
    # print intro text, tell user the word length
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is ' + str(k) + ' letters long.')
    print ('-------------')
    
    # while guessLeft is greater than zero (while user still has guesses left)
    while guessLeft > 0:
        # print how many guesses are left
        print ('You have ' + str(guessLeft) + ' guesses left.')
        
        # print available letters
        print ('Available letters: ' + getAvailableLetters(lettersGuessed))
        
        # prompt user to guess a letter
        guess = input('Please guess a letter: ')
        
        # make sure letter entered is lowercase
        guessLower = guess.lower()
        
        # add the entered letter to lettersGuessed
        lettersGuessed.append(guessLower)
        
        # if the letter guessed is already in lettersGuessed, print Oops message and show progress using getGuessedWord function
        if lettersGuessed.count(guessLower) > 1:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print ('-------------')
        
        # if the letter guessed is in secretWord, show progress (including the guess) using getGuessedWord function
        elif guessLower in secretWord:
            print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            print ('-------------')
            
            # if they've guessed the entire word, print Congrats message and break out of the loop
            if isWordGuessed(secretWord, lettersGuessed) == True:
                return 'Congratulations, you won!'
                break
        # otherwise, if letter not in secretWord, decrement guessLeft by 1 and show progress using getGuessedWord function
        else:
            guessLeft -= 1
            print ('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            print ('-------------')
    # if guessLeft is not >0, tell the user they ran out of guesses and print the secretWord
    else:
        return str('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')

#hangman(secretWord)

