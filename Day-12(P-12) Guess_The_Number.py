#  To randomly select a result number
import random

# attempts based on two different levels
Easy_Level_Turns = 10
Hard_Level_Turns = 5

# Depending on difficulty reduce the number of turns taken to reach the answer
def set_mode():
    level = input("Choose Difficulty: easy or hard >> ")
    if(level == "easy"):
        return Easy_Level_Turns
    elif(level == "hard"):
        return Hard_Level_Turns
    else:
        print("Invalid Input!")

# Check whether the guessed number is close or equal to the answer
def check(guess,answer,turns):
    if(guess > answer):
        print("Too High!")
        return turns-1
    elif(guess < answer):
        print("Too Low!")
        return turns-1
    else:
        print(f"Congratulations! The answer is {answer}")
        return
        
# MAIN GAME
print("Welcome to the Number Guessing game!")
print("Think of a number between 1 to 100")
answer = random.randint(1,100)

attempts = set_mode()
game_over = False

guess = 0
while(guess != answer or game_over == True):
    print(f"\nYou have {attempts} attempts remaining to guess the number. Choose wisely.")
    guess = int(input("Guess the number >> "))
    attempts = check(guess,answer,attempts)
    if(attempts == 0):
        print("You ran out of guesses. You Lose")
        game_over = True
    elif(guess != answer):
        print("Guess again.")










