# Rock, Paper, Scissors game
# Created 20231220
# Author: kyperkins@gmail.com

"""
I feel like I need to explain the difference, between the video tutorial and the
items below. While Tomi does a good job explaining the basics of a Python
program, the UX-developer in me said "That's a lot of repeating". I mean, 66
lines and 90% of it is print() statements.

I thought I could do better. I found my old Coursera Python script at
http://www.codeskulptor.org/#user10_nr9Aq94XQBGpn0s.py back in 2013, but even
that had a lot of fluff. Here's basically 66 lines (minus this comment),
covering any scenario, score tracking, easy input of options, user
personalization, and a docblock.

While I am in no way a Python expert, this seems to do a more effecient job
than 42 lines of print()
"""

import random

# Intial user personalization
user_name = input("What is your name? ")

# Game variables
total_games = user_score = computer_score = 0
computer_name = "Computer"

# Conver the number to a human-readable name
def number_to_name(num):
    match num:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scissors"

# Function to handle the winner (DRY)
def win_this_round(winner, score):
    return winner, score + 1

# Main Game loop
while True:
# Note: Rock < Paper
#	Paper < Scissors
#	Scissors < Rock
    options = ['1', '2', '3']

    print(f"\nGame #{total_games+1}")
    user_input = str(input("What is your choice:\n1. Rock\n2. Paper\n3. Scissors\nChoice (or 'exit'): "))
    print("You chose", user_input)
    computer_input = random.choice(options)
    
    if user_input not in options:
        print("\nGame Over")
        if (total_games > 0):
            print(f"{user_name} won {user_score} out of {total_games} games")
            percentage = (user_score / total_games)*100
            print(f"That's {percentage:.2f}%")
        quit()
    
    print(f"{user_name}: {number_to_name(int(user_input))} | Computer: {number_to_name(computer_input)}")

    # First, do start-end comparisions
    if (int(user_input)==options[-1] and int(computer_input)==options[0]):
        winner, computer_score = win_this_round(computer_name, computer_score)
    elif (int(user_input)==options[0] and int(computer_input)==options[-1]):
        winner, user_score = win_this_round(user_name, user_score)
    elif (int(user_input) < int(computer_input)):
        winner, computer_score = win_this_round(computer_name, computer_score)
    elif (int(computer_input) < int(user_input)):
        winner, user_score = win_this_round(user_name, user_score)
    elif (int(computer_input) == int(user_input)):
        winner = "Nobody - it's a tie"
        
    print("WINNER:", str(winner))
    print(f"Score: {user_name}: {user_score} | Computer: {computer_score}")
    total_games += 1;
    
    print("\n===========================\n")