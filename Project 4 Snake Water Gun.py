# Snake Water Gun

# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.

# Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.





import random
import os 
os.system('cls')

def check(comp,user):

    if (comp==user):
        return 0            # 0 Means draw

    elif (comp==0 and user==1 ):
        return -1           # These -1 means score reduced to -1

    elif (comp==1 and user==2 ):
        return -1

    elif (comp==2 and user==0 ):
        return -1

    else: return 1  # Returning score 1 if the above all fails

comp = random.randint(0, 2)         # Computer Chooses Random Int Between 0 and 1
user = int(input(" 0 = Snake\n 1 = Water\n-1 = Gun\n: "))   # User chooses numeber

score = check(comp, user)
print('You: ',user)
print('Computer: ',comp)

if (score==0):
    print('Draw!')
elif (score== -1):
    print ('You Loose')
else: print('You Won!')








