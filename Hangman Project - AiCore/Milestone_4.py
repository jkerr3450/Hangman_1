word_list = ["apple", "banana", "orange," "pear", "plum"]
#list_of_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'] 

import random

from Milestone_3 import ask_for_input

guess = input
word = random.choice(word_list)

#SELF - in this instance of the class 
class Hangman:
    def __init__ (self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))
        # num letters = len of word by difference of guessed letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

### Task 2 
    def check_guess(self, guess):
        guess = guess.lower()       
        if guess in self.word:  #check if guess is in the word
            print(f"Good guess! {guess} is in the word {self.word}")

#task 3 step 1
    
            for i in range(0,len(self.word)+1): # loops through each letter in the word
                print(self.word[i])

                if guess == self.word: #checks if guess is in word  
                    self.word_guessed[i] = guess # adds guess to the word
                    print(self.word_guessed) #replaces with guess 
                self.num_letters = self.num_letters - 1 # reduces variable number by 1

            else: 
                self.num_lives -1 #if anything else, lives reduced by 1 
                print(f"Sorry, {guess} is not int he word.") # displays message 
                print(f"you have {self.num_lives} lives left.") # displayed number of lives left
        self.list_of_guesses.append(guess) #adds guess to list of guesses
        
    def ask_for_input(self, guess):
            while True: 
                guess = input("Guess The Missing Letter")
                print(guess)

                if(len(guess) == 1) and guess.alpha(): #if lenth is = 1 and alphabetic
                    print("Invalid letter. Please, enter a single alphabetical character.")      

                if guess in self.list_of_guesses:   #if charecter has already been guessed
                    print("You have already tried that letter!")                    
            ## not working - will not display message saying letter already guessed. 

                else: self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break 



    def ask_for_input(self, guess):
        while True:
            guess = input("Guess the missing letter")
            print(guess)

            if(len(guess)==1) and guess.alpha():
                print("Oops! Invalid answer. Please enter a single aplhabetical charecter")

            elif guess in list_of_guesses:
                print("You have already tired that letter")

            else: self.check_guess(guess)
            list_of_guesses =+ guess 
## task 2 does not add guess to list of guesses or dispay message saying that letter has already been guessed
        
### Task 3 
