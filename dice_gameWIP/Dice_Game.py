#Dice Game

#import Dice
import time
import os
from Dice import D6, D4, D8, D10, D12, D20, D100
from speech import speechText

DiceTest = D6.roll(), D4.roll(), D8.roll(), D10.roll(), D12.roll(), D20.roll(), D100.roll()

#print(DiceTest)
speechText('Calibrating the dice', 0.04)
print('\n')
speechText(str(DiceTest), 0.04)
os.system('cls')

#Title Screen
def title_screen():

        os.system('cls')
        print(open('resources/title.txt').read())
        time.sleep(2)
        print()
        print("Press 'ENTER' to continue")
        input()
        os.system('cls')
        options()

#options/game modes
def options():

	os.system('cls')
	print('		-Free Roll-		')
	print('		-Spell Dice-	')
	print('		-Dice-Knights-	')
	print('		-Quit-		')
title_screen()