#function, which takes three integers a, b, and c as arguments,
# and returns True if exactly two of of the three integers are
 #positive numbers (greater than zero), and False - otherwise.

def number_checker(a,b,c):
    if a>0 and b>0 and c>0:
        return False
    elif (a>0 and b>0) or (a>0 and c>0) or (b>0 and c>0):
        return True
    else:
        return False
    
    
print(number_checker(2, 4, -3))
print(number_checker(-4, 6, 8))
print(number_checker(4, -6, 9))
print(number_checker(-4, 6, 0))
print(number_checker(4, 6, 10) )
print(number_checker(-14, -3, -4))