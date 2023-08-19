#function, which takes three integers a, b, and c as arguments,
# and returns True if exactly two of of the three integers are
 #positive numbers (greater than zero), and False - otherwise.

def number_checker(a,b,c):
    if a>0 and b>0:
        return 'True'
    elif a>0 and c>0:
        return 'True'
    elif b>0 and c>0:
        return 'True'
    elif b>0 and a>0:
        return 'True'
    else:
        return 'False'
    
    
print(number_checker(2,4,-5))