while True:
    guess = input("Guess The Missing Letter")
    print(guess)

    if(len(guess) == 1) and guess.isalpha():                                # if input is 1 value - prints good guess  
        break 

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")                     # if input is anything else - printsinvalid input   




