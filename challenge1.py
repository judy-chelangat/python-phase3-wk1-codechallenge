#Converting 12-hour time to 24-hour time
#step 1 defining a function
#return a four-digit string that encodes that time in 24-hour time.

def time(hour,min,period):
    new_hour = hour+12 
    new_min =min+00
    #if statement to check whether its' noon or midnight
    if hour == 12 and period == "am":
        return '0000hrs'
    elif hour == 12 and period =='pm':
      return '1200hrs'
    elif period == 'am': #vhecking if it's am
        return f"{hour:02d}{min:02d}"
    else:
      return f"{new_hour}{new_min} hrs"


print(time(12,00,"am"))

