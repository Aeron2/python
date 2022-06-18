from data import data
from data import logo
from data import vs
import random


def ran_account():
    return random.choice(data)


def ran_acc_data(account):
    name = account["name"]
    descrip = account["description"]
    country = account["country"]
    return f"{name}, a {descrip}, from{country}"


def check(guess, a, b):
    if a > b and guess == "a":
        return True
    elif a > b and guess == "b":
        return False
    elif a < b and guess == "b":
        return True
    elif a < b and guess == "a":
        return False


def play_game():
    print(logo)
    score = 0
    game_continue = True
    a = ran_account()
    b = ran_account()
    while game_continue:
        a = b
        b = ran_account()
        if a == b:
            b = ran_account()

        print(f"Compare A: {ran_acc_data(a)}")
        print(vs)
        print(f"With B: {ran_acc_data(b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower = a["follower_count"]
        b_follower = b["follower_count"]
        is_correct = check(guess, a_follower, b_follower)
        if is_correct:
            score += 1
            print(f"Yourre right!Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, final score: {score}")


play_game()
