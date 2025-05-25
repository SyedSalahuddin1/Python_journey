from random import randint
from art import logo4

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 8


def check_answer(guess_number,actual_answer,turns):
    if guess_number > actual_answer:
        print("Too High.")
        return turns - 1
    elif guess_number < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You have got the answer.The number is {actual_answer}.")


def set_difficulty():
    level = input("Choose difficulty,Type 'easy' or 'hard'? ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo4)
    print("Welcome to number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the answer is {answer}.")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the answer.")
        guess = int(input("Make a guess? "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses.Game Over!")
            return
        elif guess != answer:
            print("Guess again.")


game()
