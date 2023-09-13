
def game():
    
    play = True if input("Do you want to play the game? (yes/no): ").replace(' ', '').lower() == "yes" else False

    while(play == True):

        guessed = False
        guesses = 0
        target = -1

        while(target not in range(101)):
            target = int(input("Player 1, please enter a number to guess between 0 and 100 (inclusive): "))

        while guessed == False:
            guess = int(input("Player 2, please enter a guess: "))
            guesses+=1

            if(guess > 100 or guess < 0):
                print("Your guess was outside of the acceptable range (0 to 100)!")

            elif(guess > target):
                print("Your guess was too high!")
            
            elif(guess < target):
                print("Your guess was too low!")

            else:
                print("You guessed correctly!")
                guessed = True

        print(f"You took: {guesses} guesses.")
        play = True if input("Do you want to play again? (yes/no): ").lower().replace(' ', '') == "yes" else False

if __name__ == "__main__":
    game()