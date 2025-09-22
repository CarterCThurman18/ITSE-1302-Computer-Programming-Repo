while True: #While loop that allows the game to return to the beginning if you want to play again
    from random import randrange
    random_number = randrange(0, 101) #This sets the limits of the game between 0 and 100 ultimatley
    print("Guess the random number between 0 and 100 within 10 tries or you lose!\n ")
    for guesses in range(1, 11): #Allows the user to make only a certain amount of guesses
        guess = int(input(f"\nGuess #{guesses}| Enter your next guess:"))
        if random_number == guess: #Correct guess response
            print(f"You have guessed the random number {random_number} \ncorrectly with only {guesses} attempts!\n")
            break
        elif random_number != guess: # Incorrect guess statements
            print("You have guessed wrong.")
            if guesses == 10:
                print("You have ran out of guesses, you lose!")
            elif guess < random_number:
                print("The correct number is \"larger\" than the number you guessed\n============================")
            elif guess > random_number:
                print("The correct number is \"smaller\" than the number you guessed\n============================")
            
    while True: #Logic for restarting the game or quitting
        response = input("would you like to play again? (y/n):").lower()
        if response == str("y"):
            break 
        elif response == str("n"):
            print("Thanks for playing")
            print("Completed by,\nCarter Thurman")
            exit() 
        else:
            print("Invalid response")

#Completed by, Carter Thurman
                
           
                

           

        
        

