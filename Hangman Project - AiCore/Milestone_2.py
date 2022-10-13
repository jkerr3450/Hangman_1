import random

while True:
    guess = input("Guess The Missing Letter")
    print(guess)                                                            # 

    if(len(guess) == 1) and guess.isalpha():                                # if input is 1 value - prints good guess  
        break 

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")                     # if input is anything else - printsinvalid input   



word_list = ["apple"]

word = random.choice(word_list) 
# if statment that check if the input is in the random word
if(guess in word):
    print(f"Good guess! {guess} is in the word")

else:
    print(f"Sorry, {guess} is not in the word. Try again.")

#
