# Rock, Paper and Scissor Game in Python

import random

player = input("Select Rock or Paper or Scissor :").lower()
if player == "rock" or "paper" or "scissor":
    
    bot = random.choice(["Rock","Paper","Scissor"]).lower()
    print("Bot has Selected: ",bot.capitalize())

    if player == "rock" and bot == "paper":
        print("Bot Won")
    elif player == "paper" and bot == "scissor":
        print("Bot Won")
    elif player == "scissor" and bot == "rock":
        print("Bot Won")
    elif player == bot:
        print("Tie")
    else:
        print("Player Won")
        

