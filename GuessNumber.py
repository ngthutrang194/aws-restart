import  Art
#import  random
from random import randint
from replit import clear
easy_turn = 10
hard_turn = 5

def check_answer(guess, answer, turns):
     if guess > answer:
         print("too high")
         return turns -1
     elif guess < answer:
         print("too low")
         return  turns - 1
     else:
         print(f" You got it! The answer was {answer} ")

def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_turn
    else:
        return hard_turn
def game():
    print("welcome to the number Guess Game! ")
    print("I'm thingking of a number between 1 and 100")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
         print(f" you have {turns} attempts remaining to guess the number.")
         guess = int(input("Make a guess "))
         turns = check_answer(guess, answer, turns)
         if turns == 0:
             print(" you fail, Goodbye")
             break
         elif guess != answer:
             print("Guess again ")

while input("Do you want to play a game? Type 'y' or 'n' ") == "y":

    clear()
    game()




