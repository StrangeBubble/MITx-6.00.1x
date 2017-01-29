def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp < 2:
        return base
    else:
        return base * recurPower(base, exp-1)

print recurPower(2, 1)
print recurPower(20, 1)
print recurPower(2, 5)
print recurPower(5, 5)
print recurPower(5, 50)

