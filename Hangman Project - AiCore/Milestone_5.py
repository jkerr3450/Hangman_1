# word_list = ["apple", "banana", "orange," "pear", "plum"]
# list_of_guesses = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'] 

word_list = ["pineapple", "melon", "strawberry", "mango", "watermelon"]

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
        self.guess = input

### Task 2 
    def check_guess(self, guess):
        guess = guess.lower()     # Changes input to lower case   
        if guess in self.word:  #check if guess is in the word
            print(f"Good guess! {guess} is in the word.")
        
#task 3 step 1
    
            for i in range(0,len(self.word)): # loops through each letter in the word

                if guess == self.word[i]: #checks if guess is in word  
                    self.word_guessed[i] = guess # adds guess to the word
                    print(self.word_guessed)
            self.num_letters = self.num_letters - 1
                

        else: 
            self.num_lives = self.num_lives - 1 #if anything else, lives reduced by 1 
            print(f"Sorry, {guess} is not in the word.") # displays message 
            print(f"You have {self.num_lives} lives left.") # displayed number of lives left 

        self.list_of_guesses.append(guess) #adds guess to list of guesses
    
    def ask_for_input(self):
        while True: 
            guess = input("Guess The Missing Letter")
            print(guess) 
            #print (self.list_of_guesses)

            if guess in self.list_of_guesses:   #if charecter has already been guessed
                print("You have already tried that letter!")          

            if(len(guess) == 1) and guess.isalpha(): 
                pass                               

 # if input is anything else - prints invalid input   
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")             
#################   ## not working - will not display message saying letter already guessed. ######################
            
            
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            break 

## task 2 does not add guess to list of guesses or dispay message saying that letter has already been guessed
    
    ## Milestone 5 

def play_game(word_list): # creating a function with word list passed in as a parameter
    num_lives = 5 # defining a number of lives in this arguments
    game = Hangman(word_list, num_lives) #creating an instance of the hangman class and assigning it to a the variable game

    while True: 

        if(game.num_lives == 0):
            print(f"You Lost! The word was {game.word}")
            break

        elif(game.num_letters > 0):
            game.ask_for_input()

        elif(game.num_lives > 0 and game.num_letters == 0):
                print("Congratulations. You won the game!")
                break
    
play_game(word_list)

#Create a function that will run all the code to run the game as expected. You should begin by creating a new script called milestone_5.py. Copy all the codes in milestone_4.py file into the newly created milestone_5.py file.

#Step 1. Create a function called play_game that takes word_list as a parameter. Inside the function, write the code for the following steps

#Step 1. Create an instance of the Hangman class. Do this by calling the Hangman class and assign it to a variable called game.

#Step 2. Pass word_list and num_lives as arguments to the game object.

#Step 3. Create a while loop and set the condition to True. In the body of the loop, do the following
    #1. Check if the `num_lives` is 0. If it is, that means the game has ended and the user lost. Print a message saying 'You lost!'.
    #2. Next, check if the `num_letters` is greater than 0. In this case, you would want to continue the game, so you need to call the `ask_for_input` method. 
    #3. If the `num_lives` is not 0 and the `num_letters` is not greater than 0, that means the user has won the game. Print a message saying 'Congratulations. You won the game!'.

#Step 2. Outside the function, call your play_game function to play your game. Don't forget to pass in your list of words as argument to the function.