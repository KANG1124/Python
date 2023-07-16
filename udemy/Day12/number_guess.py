import random

print("Welcome to the Number Guessing Game!")
print("I'm Thinking of a Number Between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

num = 0
player_num = 0

def number():
    number_list = list(range(1, 101))
    num = random.choice(number_list)
    return num

def compare_easy(num, player_num):
    attempt_times_easy = 10
    while attempt_times_easy > 0:
        if num == player_num:
            print(f"You get it! The answer was {num}.")
            break
        elif num < player_num:
            print("Too High.\nGuess Again.")
            print(f"You have {attempt_times_easy - 1} attempts remaining to guess number.")
            player_num = int(input("Make a guess: "))
            attempt_times_easy -= 1
        elif num > player_num:
            print("Too Low.\nGuess Again.")
            print(f"You have {attempt_times_easy - 1} attempts remaining to guess number.")
            player_num = int(input("Make a guess: "))
            attempt_times_easy -= 1

def compare_hard(num, player_num):
    attempt_times_hard = 5
    while attempt_times_hard > 0:
        if num == player_num:
            print(f"You get it! The answer was {num}.")
            break
        elif num < player_num:
            print("Too High.\nGuess Again.")
            print(f"You have {attempt_times_hard - 1} attempts remaining to guess number.")
            player_num = int(input("Make a guess: "))
            attempt_times_hard -= 1
        elif num > player_num:
            print("Too Low.\nGuess Again.")
            print(f"You have {attempt_times_hard - 1} attempts remaining to guess number.")
            player_num = int(input("Make a guess: "))
            attempt_times_hard -= 1
    if attempt_times_hard == 0:
        print("Game Over")

if difficulty == "easy":
    num = number()
    print("You have 10 attempts remaining to guess the number.")
    player_num = int(input("Make a guess: "))
    compare_easy(num, player_num)

if difficulty == "hard":
    num = number()
    print("You have 5 attempts remaining to guess the number.")
    player_num = int(input("Make a guess: "))
    compare_hard(num, player_num)