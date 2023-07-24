# PROGRAM to DECODE AND ENCODE A WORD USIGN A SECRET LANGUAGE
# CREATED BY: Ravi Shankar

import os
import random
import string

os.system('cls')

def rG():
    # string.ascii_lowercase will grab all the lower case alphabets from teh string modules
    # And random.choise will select the random letter from it 
    return random.choice(string.ascii_lowercase)

# Code for Encoding
def encoding():
    os.system('cls')
    toEncode = input("Enter the word to Encode: ")
    toEncode = toEncode.lower()

    if (len(toEncode)>=3):
              
        # Grab the first string
        first = toEncode[0]
        # set teh remainging string
        rest = toEncode[1:]  
        firstShiftedToLast = rest+first

        # Compelte Encoded 
        completeEncoded = rG()+rG()+rG()+firstShiftedToLast+rG()+rG()+rG()
        return completeEncoded

    else:
        # if the letters are less than 3 then it will just reverse it 
        return toEncode[::-1]

# Code for Decoding 
def decoding():
    os.system('cls')
    toDecode = input("Enter the word to Decode: ")
    toDecode = toDecode.lower()
    
    if(len(toDecode)<3):
        return toDecode[::-1]
    
    else:
        starting3_removed = toDecode[3:]
        ending3_removed = starting3_removed[:-3]
        lastLetter = ending3_removed[-1]
        a = lastLetter+ending3_removed
        completeDecoded = a[:-1]

        return completeDecoded


try:
    print("\nSECRET CODE LANGUAGE\n")
    options = input(('''1 - To Encode\n2 - To Decode

    '''))

    if int(options)==1:
        Encoded = encoding()  
        print("Encoded: ",Encoded)
    elif int(options)==2:
        Decoded = decoding()
        print("Decoded: ",Decoded)
    
    else:
        raise ValueError('The values are not within the specified Range')

except:
    os.system('cls')
    print("\n\n\nWRONG INPUT: START AGAIN :( \n\n\n\n")
