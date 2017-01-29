# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Lecture 5, problem 8

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    low = 0
    high = len(aStr)-1
    middle = (high + low)
#    print(aStr, len(aStr),aStr[middle:],aStr[:middle],low, high, middle, char)
    if aStr == "" :
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[middle] == char:
        return True
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle-1])
    else:
        return isIn(char, aStr[middle+1:])

