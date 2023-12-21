# Rock, Paper, Scissors game
# Created 20231220
# Author: kyperkins@gmail.com

import random

total_games = user_score = computer_score = 0
computer_name = "Computer"
user_name = input("What is your name? ")

def number_to_name(num):
    name = ""
    match num:
        case 1:
            name = "Rock"
        case 2:
            name = "Paper"
        case 3:
            name = "Scissors"
    return str(name)

def win_this_round(winner, score):
    score += 1;
    return winner, score

while True:
# Note: Rock < Paper
#	Paper < Scissors
#	Scissors < Rock
    options = [1, 2, 3]

    print("Game #"+str(total_games+1))
    user_input = input("What is your choice:\n1. Rock\n2. Paper\n3. Scissors\nChoice (or 'exit'): ")
    print("You chose", user_input)
    computer_input = random.choice(options)
    
    #not necessary, but helpful for UX
    print("Thinking...\n") 
    
    if int(user_input) not in options:
        print("Game Ended")
        if (total_games > 0):
            print(str(user_name)+" won", str(user_score),"out of",str(total_games),"games")
            percentage = (user_score / total_games)*100
            print("That's %.2f" % percentage + "%")
        quit()
    
    print(str(user_name)+": "+number_to_name(int(user_input))+" | Computer: "+number_to_name(computer_input))

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
    print("Score: "+str(user_name)+": "+str(user_score)+" | Computer: "+str(computer_score))
    total_games += 1;
    
    print("\n===========================\n")