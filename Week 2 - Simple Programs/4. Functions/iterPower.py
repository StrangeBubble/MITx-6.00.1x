# Exercise: iter power

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 6 minutes

# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication.
# For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

# This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical
# value. Your code must be iterative - use of the ** operator is not allowed.


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    x = 1
    if exp < 1:
        return 1
    while exp > 0:
        exp-=1
        x*=base
    return x

print iterPower(6.61, 0)
print iterPower(5.9, 10)
print iterPower(-4.75, 8)

print iterPower(3, 2)
print iterPower(3, 5)
print iterPower(5, 5)
