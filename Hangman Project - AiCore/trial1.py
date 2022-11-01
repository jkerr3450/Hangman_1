### Milestone 4
import random

word_list = ['peach', 'pineapple', 'orange', 'strawberry', 'mango']


# Task 1
class Hangman:
    def __init__ (self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word)
        self.num_letters = len(set(self.word)(set(self.word_guessed)))
        self.num_lives = num_lives
        self.word_list = word_list 
        self.list_of_guesses = [""]
        
# Task 2. Step 1
    def check_guess(self, guess):
        guess = guess.islower()
        
#.2 & .3
        if guess in self.word:
            print(f"Good guess, {guess} is in the word.")
# Task 3
        # extend to replace underscoresin the word_guessed with the user input?? 
# .1 
        for i in range(0,len(self.word)+1): 
            print(self.word[i])
#.1 & 2
        if guess == self.word:   
                self.word_guessed[i] = guess 
                print(self.word_guessed) 
#.3        
                self.num_letters = self.num_letters - 1 
# Task 4 
        else: 
            self.num_lives - 1 
#.2
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} left.")

# Task 4 Step 3 
        self.list_of_guesses.append(guess)

# Task 2 
    def ask_for_input(self):
        while True:
            guess = input("Guess the missing letter ")
            print(guess) 
#.4
            if (len(guess) > 1) and guess.numeric():
                print("invalid answer. Please enter a single alphabetic charecter")
#.5 & 6
            elif guess in self.list_of_guesses:#######
                print("You have already tried that letter")
#.1
            else: 
                self.check_guess(guess) ###### cannot defint check_guess as it will overwrite class 
                self.list_of_guesses += guess
# Step 2
Hangman.ask_for_input(self)



## Milestone 5 Task 1

#Step 1 & 2 
def play_game(self, word_list):
        game = Hangman()
        word_list = ['peach', 'pineapple', 'orange', 'strawberry', 'mango']
        num_lives = 5
# .3 
        while True:
            if game.num_lives == 0:
                print('You lost! ')

            elif    game.num_letters > 0:
                game.ask_for_input() 

            elif num_lives >0 and self.num_letters == 0:
                print('Congratulations. You won the game!')
# Step 2
Hangman.play_game()









        





## line 54 - self not defined? 
## line 58 - check guess not defined?