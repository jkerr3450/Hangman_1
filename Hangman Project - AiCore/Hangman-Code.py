import abc
import random

word_list = ["apple", "banana", "orange", "pear", "strawberry"]

word = random.choice(word_list)
print(word)

guess = input("Guess the missing letter")
print(guess)

if(len(guess) == 1) and guess.isalpha():
        print("Good Guess!")   
else:
    print("Oops! Invalid answer!") 

while True:
    guess = input("Guess the missing Letter")

