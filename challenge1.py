#Converting 12-hour time to 24-hour time
#step 1 defining a function
#return a four-digit string that encodes that time in 24-hour time.

def time(hour,min,period):
    new_hour = hour+12 
    new_min =min+00
    #if statement to check whether its' noon or midnight
    if hour == 12 and min == 00:
        return (f"{hour}{min}0 {period}")
    else:
      return (f"{new_hour}{new_min} hrs")


print(time(12,00,"am"))

