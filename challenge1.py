#Converting 12-hour time to 24-hour time
#step 1 defining a function
#return a four-digit string that encodes that time in 24-hour time.

def time(hour,min,period):
    new_hour = hour+12 
    new_min =min+00
    return (f"{new_hour}{new_min} hrs")


print(time(10,24,"am"))
