# Exercise: fourth power

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 2 minutes

# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier exercise exercise (you don't need to redefine square in this box;
# when you call square, the grader will use our definition).

# This function takes in one number and returns one number.

def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    divisor = 0

    # Test to see which variable is smaller
    if a < b:
        divisor = a
    elif a > b:
        divisor = b
    else:
        divisor = a

    while divisor > 1:
        if a%divisor == 0:
            if b%divisor == 0:
                return divisor
        divisor -= 1
    return 1

