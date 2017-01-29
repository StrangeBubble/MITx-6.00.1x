# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

# You should use the square procedure that you defined in Problem 3 of these lecture exercises (you don't need to redefine square in this box; when you call square, the tutor will use our definition).

# This function takes in one number and returns one number.

def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x**2


def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))

print fourthPower(5)

