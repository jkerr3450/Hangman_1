# Hangman
## Project No.1 

Through milestones 1 & 2 of this project, I have coded the basics of a game of Hangman. I have inistalised a repository on GITHub where the code can be update through a read.me file, comitted and cloned. 

The programme will carry out this task by selecting a random word from a world list before asking for user input. The user input will be validated through the use of 'if' statements that checks the length and context of what has been entered. 

## Milestone 1 

The first step was to set up the GIT enviroment. GIT is used to run the command line. From here, i then intialised a repository on GITHub and updated the read.me file. 

Once updated, i was able to modify , stage, comit and clone my files from my system to initalise the project. 

### Git commands: 
```git init```       to create repository.

```git add```   which moves files to a staged state. 

```git comit```  comits all files in the staged state. 


## Milestone 2 
### Task 1 - Define a list of possible words 
 
 To complete the following task, i have classified a list of varibles containing the name of 5 fruits. 

These variables have been added to the class 'word_list'

```word_list = ["apple", "banana", "orange", "pear", "strawberry"]```

### Task 2 - Choose a random word from the list. 
 For my code to select a random word from the list, I have ued the random method which selects a random variable from the word_list: 

 ```word = random.choice(word_list)```
 
Once selected, the print function will allow the code to print the random variable from the word list. 

```print(word)```
### Task 3 - Ask user for input function. 

 The next step in my code is to ask the user for input. This is acheived by using the input function. With this, the user will be prompted for an input by displaying the message "Guess the missing ketter". 

 ```guess = input("Guess the missing letter")```
```print(guess)```

### Task 4 - validate user input

 The final task of milestone 2 requires the user input to be validated. For this, i used "if" statements to validate both the length and context of the input.

 The code has been created so that it checs that the input if 1 charetcer and alphabetical. 

```if(len(guess) == 1) and guess.isalpha()```   

If both conditions are met, then a print function will display the folliwng message:

            "Good Guess!"

An "else" parameter has been added to the 'if' statments to determine the actions if the user enters an invalid input. 

The else parameter will come in to play when any condition is not met. 

Therfore, if the input is not a sinlge alphabetic charecter, then the folliwng error messgae is displayed: 

        "Oops! invalid answer!"

To complete this block, I have added a 'while True' statment. The purpose of this is to restart the cycle only whenever a valid input has been entered. This will allow continuity between the user being asked for an input and the code validating it.

```while True:```
    ```guess = input("Guess the missing Letter")```

As shown above, whilst the user input is vald, the code wil then continue and ask the user to guess another letter. 

## Milestone 3

### Task 1 - Iterativley check if the input is a valid guess 

To validate the users input, i created a 'while' loop with the condition set to true. The purpose of this is to ensure the code runs smoothly if the parameters of the while loop are true based on the users input. 

The loop validates the inout by checking if it is a single aplhabetical letter using the following code: 

```if(len(guess) == 1) and guess.isalpha()```

If this passes, the code will break they while loop. 
If either of the 2 conditions return false, then an error message is displayed showing: 

    Invalid letter. Please, enter a single alphabetical character.

### Task 2 - Check if the guess is in the word

The purpose of the 'if' statement is to verify if the users guess is in the word seleccted from the list. 

If so, the user will see a message stating that the guess is in the word. 

```if(guess in word):```
        ```print(f"Good guess! {guess} is in the word")```

To ensure that the if statment worked correctly and that the actual guessed letter was displayed instead of {guess}, i had to assign the word guess to a variable. 

The next step was to code an else block that determined the actions if the guess was not in the selected random word. 

```else:```

```print(f"Sorry, {guess} is not in the word. Try again.")```

### Task 3 - Create a function to run checks 

The final task was the create a function to run the checks that i have set out. 

to do this, i have defined a fucntion that will check the users input for the required data. 

Once the function has been called
'```ask_for_inpit()```'
the checks will run automatically, validating if the user input is a single alphabetical charecter. The steps highlighted in task 2 will be perfomred depending on if the while loop within the function returns true or false. 


