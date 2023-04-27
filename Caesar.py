#Code for Caesar Cipher Project
#Author: Jaleel Williams (ID @03057383)

import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R',  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

count = 0 #integer variable that  the amount of characters printed to the screen
x = int(sys.argv[1]) #integer variable given as a parameter. Represents the magnitude of the shift

for line in sys.stdin: #reads each line from a text file given as a parameter

    for letter in line: #reads each character in a given line from the input file

        letter = letter.upper() #converts any alphabetical character to uppercase
        if(letter in alphabet): #checks to see if the character is an uppercase letter
                
            new_index = alphabet.index(letter) + x #integer representing the index of the shifted letter in the list alphabet

            if(new_index > 25): #checks if the index is out of range of the list alphabet.

                new_index -= 26; #the index is corrected to give the proper letter corresponding to the shift.
                
            print(alphabet[new_index], end="")
            count += 1

            if(count % 50 == 0): #for every 50 characters one a line, a newline character is printed

                print("\n", end="")

            elif(count % 5 == 0): #for every 5 characters one a line, a whitespace is printed

                print(" ", end="")

