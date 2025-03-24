from random import randint

EASY_TURNS=10
HARD_TURNS=5

print("Welcome to the Number Guessing Game")
def check_answer(user_number,actual_number,turns):
    if user_number>actual_number:
        print("Too High")
        return turns-1
    elif user_number<actual_number:
        print("Too low")
        return turns-1
    else:
        print(f"Correct Number was {actual_number}, You Win")
        return turns

def set_difficulty():
    level=input('Choose a difficulty, Easy or Hard? Type "easy" or "hard"')
    if level=="easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    print("I'm thinking of a number between 1 and 100")
    answer=randint(1,100)
    #print(f"The number is {answer}")

    turns=set_difficulty()

    guess=0
    while guess!=answer and turns>0:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess=int(input("Make a Guess"))
        turns=check_answer(guess,answer,turns)
        if turns==0 and guess!=answer:
            print("Out of guesses, Game Over")
            return

game()
