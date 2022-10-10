# Hangman
## Project No.1 'Hangman' Milestones 1 &amp; 2. 

Through milestones 1 & 2 of this project, I have built a programme that will compelte a simple game of hangman. I have inistalised a repository on GITHub where the code can be update through a read.me file, comitted and cloned. 

The programme will carry out this task by selecting a random word from a world list before asking for user input. The user input will be validated through the use of 'if' statements that checks the length and context of what has been entered. 

## Milestone 1 

The first step was to set up the GIT enviroment. GIT is used to run the command line. From here, i then intlised a repository on GITHub and updated the read.me file. 

Once updated, i was able to modify , stage, comit and clone my files from my system to initalise the project. 

### Git commands: 
```git init```       to create repository.

```git add```   which moves files to a staged state. 

```git comit```  comits all files in the staged state. 


## Milestone 2 
### Task 1 
 - Define a list of possible words 
 
 To complete the following task, i have classified a list of varibles containing the name of 5 fruits. 

These variables have been added to the class 'word_list'

```word_list = ["apple", "banana", "orange", "pear", "strawberry"]```

### Task 2 
 For my code to select a random word from the list, I have ued the random method which selects a random variable from the word_list: 

 ```word = random.choice(word_list)```
 
Once selected, the print command will allow the code to print the random variable from the word list. 

```print(word)```
### Task 3 
 - Ask user for input function. 

 The next step in my code is to ask the user for input. This is acheived by using the input function. With this, the user will be promted for an input by displaying the message "Guess the missing ketter". 

 ```guess = input("Guess the missing letter")```
```print(guess)```

### Task 4 
 - validate user input

 The finlal task of milestone 2 requires the user input to be validated. For this, i used "if" statements to validate both the length and context of the input.

 The code has been created so that it checs that the input if 1 charetcer and alphabetical. 

```if(len(guess) == 1) and guess.isalpha()```   

If both conditions are met, then a print comman will display the folliwng message:

            "Good Guess!"

An "else" statment has been created in the same block as the 'if' statments to determine the actions if the user enters an invalid input. 

The else statments will come in to play when any condition is not met. 

Therfore, if the input is not 1 charecter or alphabetic, then the folliwng error messgae is displayed: 

        "Oops! invalid answer!"

An additional function has been entered wwhich will allow the game to recycle through the sequences.  

This is acheived with the use of a "while True" fucntion. The purpose of this is to restart the cycle only whenever a valid input has been entered. This will allow continuity between the code asking for user input and the input validation sequence. 

```while True:```
    ```guess = input("Guess the missing Letter")```

As shown above, whilst the user input is vald, the code wil then continue and ask the user to guess another letter. 