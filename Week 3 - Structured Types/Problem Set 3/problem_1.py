# Problem 1
# 10/10 point (graded)
# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily
# code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list
# of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord
# are in lettersGuessed) and False otherwise.

# Example Usage:
# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(isWordGuessed(secretWord, lettersGuessed))
# False

# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # set variables true and false equal to zero
    true = 0
    false = 0

    # iterate through the chars in secretWord
    for char in secretWord:

        # if the char is in lettersGuessed, increase true by 1
        if char in lettersGuessed:
            true += 1

        # if the char is not in lettersGuessed, increase false by 1
        else:
            false +=1

    # if false is zero, return True
    if false == 0:
        return True

    # otherwise, return False
    else:
        return False

