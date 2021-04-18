import random

def play():
    user = input("what's your choice 'rock', 'paper', 'scissors'\n")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return "It's tie"

    if is_win(user, computer):
        return "You Won"

    return "You Lose"

def is_win (player, opponent):
    if (player == 'rock' and opponent == 'scissors') or (player == 'paper' and opponent == 'rock') or (player == 'scissors' and opponent == 'paper'):
        return True

print(play())