from random import choice 


player =input("rock (r), paper (p) or scissors (s)?  ")
if player == 'r' : player= "0"
elif player=='p' : player= "___"
else :player=">8"
computer = choice(['0','___','>8'])

print ( "Player : ",player , " vs " , computer," : Computer" )
if player == computer : print("Draw !!")
elif player == '0' :
    if computer == '___': print("Computer wins !!")
    else : print("Player wins !!")
elif player == '___':
    if computer == '0': print("Player wins !!")
    else : print("computer wins !!")
else :
    if computer == '0': print("Computer wins !!")
    else : print("Player wins !!")

