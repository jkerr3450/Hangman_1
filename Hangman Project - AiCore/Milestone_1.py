import abc 
import random

word_list = ["apple", "banana", "orange," "pear", "plum"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "x", "y", "z"]

word = random.choice(word_list)
print(word)

guess = input("Guess The Missing Letter")
print(guess)

if(len(guess) == 1) and guess.isalpha():                                # if input is 1 value - prints good guess 
        print("Good Guess!")   
else:
    print("Oops! Invalid answer!")                     # if input is anything else - printsinvalid input   

while True:
    guess = input("Guess the missing Letter")          # re runs the check until something is invalid 
#command needed with while true statment e.g whilst true and on last life

 


