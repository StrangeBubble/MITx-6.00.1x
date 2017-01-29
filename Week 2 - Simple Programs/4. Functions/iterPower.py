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
