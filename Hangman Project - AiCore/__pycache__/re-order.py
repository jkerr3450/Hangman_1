word_list = ["apple", "banana", "orange," "pear", "plum"]
#list_of_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'] 

import random
word = random.choice(word_list)

#SELF - in this instance of the class 
class Hangman:
    def __init__ (self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = len(set(self.word))# num letters = len of word by difference of guessed letters
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []




def check_guess(self, guess):
        guess = guess.lower()     # Changes input to lower case   
        if guess in self.word:  #check if guess is in the word
            print(f"Good guess! {guess} is in the word.")

            for i in range(0,len(self.word)): # loops through each letter in the word
                print(self.word[i])

                if guess == self.word[i]: #checks if guess is in word  
                    self.word_guessed[i] = guess # adds guess to the word
                    print(self.word_guessed) #replaces with guess 
                    
            self.num_lives -= 1 



def ask_for_input(self):
        while True: 
            guess = input("Guess The Missing Letter")
            print(guess) 
            print (self.list_of_guesses)

            if guess in self.list_of_guesses:   #if charecter has already been guessed
                print("You have already tried that letter!")          

            elif(len(guess) == 0) and guess.isalpha(): #if lenth is = 1 and alphabetic
                print("Invalid input. Please, enter a single alphabetical character.")

            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break 