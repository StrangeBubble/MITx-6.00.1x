def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    x = 1
    for n in xrange(0, exp):
        x *= base
    return x

print iterPower(3, 2)
print iterPower(3, 5)
print iterPower(5, 5)
