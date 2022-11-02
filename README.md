# AiCore - Hangman

## Milestone 1 - Setting up the environment. 
Through milestone one of the project, I have set up the environment of which my code can be cloned, edited and viewed by others. 

Firstly, I set up the GIT environment which is used to run the command line. From here, I then initialised a repository on GITHub where my work can be stored and viewed. 

Once created, I was able to modify, stage, commit and clone my files from my system to initialise the project. 

### Git commands: 
```git init``` to create repository.

```git add``` which moves files to a staged state. 

```git commit`` commits all files in the staged state. 


## Milestone 2 - Creating Variables 

A variable is a word assigned to an object, in this case, the objects of my code were fruits. The variable name given to them was 

```word_list = ["pineapple", "melon", "strawberry", "mango", "watermelon"]```

The aim of the game was for a random word to be chosen from this list and the user then guesses each letter. To do this, I used both the 'random' and 'input' methods. 

 ```word = random.choice(word_list)```
 
This code selects a random word from the list and assigns it to the variable 'word'. 

 The next step in my code is to ask the user for input. This is achieved by using the input function. With this, the user will be prompted for input by displaying the message "Guess the missing letter". 

 ```guess = input("Guess the missing letter")```
```print(guess)```

For the user input to be valid, the code will check if the input is a single alphabetical character. I have created and 'if' statement to carry out this task which allowed me to determine the actions if the input was invalid. 

```if(len(guess) == 1) and guess.isalpha()``` 

If both conditions are met, then a print function will display the following message:

 "Good Guess!"

An "else" statement has been added so that in the case that the requirements are not met, the following error message is displayed: 

```else:```
 ```print("Oops! invalid answer!")```


## Milestone 3 - Checking If The Guess Is In The Word

To validate the users input, I created a 'while' loop with the condition set to true. The loop asks the user for input and validates it by checking if it is a single alphabetical letter using the following code: 

```while True:```
 ```guess = input("Guess the missing Letter")```
 
 ```if(len(guess) == 1) and guess.isalpha()```
 ```break```

If this passes, the code will break the while loop. 
If either of the 2 conditions returns false, then an error message is displayed showing: 

 Invalid letter. Please, enter a single alphabetical character.

Now that I have coded the logic of the game to determine if the input is valid or invalid, the next step was to create the checks to determine if the input is in the word. 

I acheived this through the use of another if statement 

```if(guess in word):```
 ```print(f"Good guess! {guess} is in the word")```

The else method is added to the if block which creates the outcome if the input is not in the word. 

```else:```

```print(f"Sorry, {guess} is not in the word. Try again.")```

Furthermore, I then created functions to house the code that asks for user input and checks the user input. The use of functions allows for the code to be read easily, structured more clearly and avoids repetition. 

## Milestone 4 - Creating the class 

At this stage, I have created the hangman class which will allow me to create a template for the object. Within this class, I have defined the functions, methods and parameters which are to be completed once the class is called. 

The class has been initiated through the ```__init__``` method which means that these method/methods are run every time a new instance is initialised. 

```num_lives``` and ```word_list``` have both been passed in as parameters of this class. 

``` def Hangman(Nume_lives, word_list)```

I then initiated the instances of the class through the ```self```. The reason for this is because 'self', is a variable that represents the instance of the class. 

Once complete, I created methods running the class and defined what happens if the user input is not in the selected random word. 

Within the hangman class, the 'check guess' method has been created. 

Firstly, the code checks if the input is in the word. This is achieved through an if statement. 

In this method, I have also determined the actions depending on if the user input is in the random word, or if it is not. 

I did this by running a for loop that cycles through each letter of the word, checking that the letter is equal to the guess and replacing the corresponding [_]. 

```if guess == self.word: #checks if guess is in word ``` 
 ```self.word_guessed[i] = guess # adds guess to the word```
 ```print(self.word_guessed) #replaces with guess```
 ```self.num_letters = self.num_letters - 1 # reduces variable number by 1```

When the guess is not in the word, the users lives are reduced by 1 and a message is displayed showing stating both that the guess is incorrect and the number of remaining lives. The guess is then added to the list of guesses. 


else: 
 self.num_lives - 1 #if anything else, lives reduced by 1 
 print(f"Sorry, {guess} is not int he word.") # displays message 
 
 print(f"You have {self.num_lives} lives left.") # displayed number of lives left
 self.list_of_guesses.append(guess)


I then defined another method within the hangman class which asks the user for input. The code in the body of this method checks the context of the input and ensures it is valid through the if statement. 

 if(len(guess)==1) and guess.alpha():
 
 print("Oops! Invalid answer. Please enter a single alphabetical character")

Additionally, I have used the elif function to determine the actions if the letter has already been guessed. If it has not yet been guessed, the code will add the letter to the list_of_guesses.

# Milestone 5 - Code the Logic of The Game

Finally, now that I have coded the basics of the game, I can put it together.

For this, i created a new function names 'play_game' and once again, passed the word_list in as a parameter.

def play_game(word_list)

I then created an instance of the hangman class and assigned it to the variable 'game'. 'word_list' and 'guess' were passed in as arguments. 

Lastly, I created another while loop which checked if the `num_lives` is 0, if the `num_letters` is greater than 0 and if the `num_lives` is not 0 and the `num_letters` is not greater than 0. 

The corresponding print message was displayed depending on which statement matched. 

 if(game.num_lives == 0):
 print(f"You Lost! The word was {game.word}")
 break

 elif(game.num_letters > 0):
 game.ask_for_input()

 elif(game.num_lives > 0 and game.num_letters == 0):
 print("Congratulations. You won the game!")
 break
 
