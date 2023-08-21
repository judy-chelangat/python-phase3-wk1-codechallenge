#Given a lowercase string that has alphabetic characters only and no spaces, 
#return the highest value of consonant substrings.
# Consonants are any letters of the alphabet except "aeiou".
#We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

def highest_value(string):
    max_value=0  #value to keep track of max value
    consonants ='bcdfghjklmnpqrstvwxyz'
    number_value =0 
    for letter in string: #looping through each letter of the string
        if letter in consonants: #checking if the letters are in the consonants
         number_value += ord(letter) - ord('a') + 1 #calculating the consonant value
        if number_value > max_value:
                max_value = number_value
        else:
            number_value =0

            return max_value
        
        

print(highest_value("zodiacs"))