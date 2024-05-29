'''
Projekt 2.py: 

__author__  = "Filip Nemlin"
__version__ = "1.0.0"
__email__   = "filip.nemlin@elev.ga.ntig.se"
'''

import msvcrt
import os

os.system("cls")
from colors import bcolors
import random
from random import randint
from functions import *
from msvcrt import getwch
import time
from time import sleep


print(bcolors.BLUE + "Hello and welcome to RPS. I hope you will enjoy the game, lets play!" + bcolors.DEFAULT)

time.sleep(1)

wins=0
losses=0
ties=0
rounds=0

while True:

        r=str(1)
        p=str(2)
        s=str(3)

        ai=random.randint(1, 3)


        print(bcolors.DEFAULT + "Choose Rock, Paper or Scissors. You can press q at any time to quit.")

        user=msvcrt.getwch().lower()
        os.system("cls")
        if user=="q":
                print("Do you want to play again? YES/NO")
                restart=msvcrt.getwch().lower()
                if restart=="y":
                        wins=0
                        losses=0
                        ties=0
                        rounds=0
                        continue
                elif restart=="n":
                        os.system("cls")
                        print("Okay, thank you for playing!\nhere is the score.")
                        print(bcolors.YELLOW + "rounds -", rounds)
                        print("wins -",wins)
                        print("losses -",losses)
                        print("ties -",ties)
                        break

        if user not in ["r", "y", "p", "s"]:
                print("Invalid choice. Please choose R, P or S")
                continue


        print("Your choise was", choises(user))
        print("AI's choise was", choises(ai))


        if user == "r":
                rounds+=1
                if ai == 1:
                        print("It's a tie!")
                        ties += 1
                elif ai == 2:
                        print("AI WON!")
                        losses += 1
                else:
                        print("YOU WON!")
                        wins += 1
        elif user == "p":
                rounds+=1
                if ai == 1:
                        print("YOU WON!")
                        wins += 1
                elif ai == 2:
                        print("It's a tie!")
                        ties += 1
                else:
                        print("AI WON!")
                        losses += 1
        elif user == "s":
                rounds+=1
                if ai == 1:
                        print("AI WON!")
                        losses += 1
                elif ai == 2:
                        print("YOU WON!")
                        wins += 1
                else:
                        print("It's a tie!")
                        ties += 1

        print(bcolors.YELLOW + "rounds -", rounds)
        print("losses -",losses)
        print("wins -",wins)
        print("ties -",ties)


