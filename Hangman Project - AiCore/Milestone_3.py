import random

### Mikestone 3 Task 1 ###
while True:
    guess = input("Guess The Missing Letter")
    print(guess)                                                            # 
# if input is 1 value and alphabetical - prints good guess  
    if(len(guess) == 1) and guess.isalpha():                                
        break 
 # if input is anything else - prints invalid input   
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")                    


#### Milestone 3 Task 2 - if the letter is in the word ####

word_list = ["apple", "banana", "orange," "pear", "plum"]

word = random.choice(word_list) 

if(guess in word):# if statment that check if the input is in the random word
    print(f"Good guess! {guess} is in the word")# if the input is anything else, print the message Sorry, {guess} is not in the word. Try again.

else:
    print(f"Sorry, {guess} is not in the word. Try again.") # else statement prints the message if guess is not in the word

### Milestone 3 Task 3 - Creating Functions ###

def check_guess(guess): 
    guess.lower()       # changes guess to lower case 
    if(guess in word): # if the input is not in the word, print the message Sorry, {guess} is not in the word. Try again.
        print(f"Good guess! {guess} is in the word")

    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(*guess):
        
        while True:
            guess = input("Guess The Missing Letter") 
            print(guess)                                                            
 
            if(len(guess) == 1) and guess.isalpha():    # if input is 1 value and alphabetical - prints good guess                             
             break 
  
            elif guess in word:
                pass
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")  # if input is anything else - prints invalid input       
                check_guess(guess)((guess in word))


ask_for_input() # call the function  - does not working with ()

