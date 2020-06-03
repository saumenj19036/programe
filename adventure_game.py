import time   # import time to sleep some times
import random   # import random to select random
# Configure list of objects
Places = ['Forest', 'Desert', 'House']
Weapons = ['Sword', 'Knife', 'Gun', 'Rock']
Forest_Monsters = ['Bear', 'Rabbit', 'Lion', 'Wolf', 'Monkey']
Desert_Monsters = ['Alien', 'Giant Monsters', 'Snake', 'Dog']
House = ['Eat', 'Drink', 'Sleep', 'Wadh Movie']
Game_Result = ['Win', 'Loose']
# End Configuration
# Define function to print messages


def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)


PrintSleep('Welcome to the game of adventures fun game', 2)
PrintSleep('Takes you to another world of fun and thrill', 2)
PrintSleep('We will help you during the game choices', 2)
PrintSleep('You have to think well before each selection so you can win', 2)
name = input('Please Enter Your Name To Start Game \n')
time.sleep(2)
print('Please choose Which place you want to play \n')
time.sleep(2)
for place in Places:
    print(place)
time.sleep(1)
Choise = ''
while Choise not in Places:
    msg = 'Give me your choise:\n'
    Choise = input(msg)
    Choise = Choise.lower()
    if Choise.lower() == 'Forest' or Choise.lower() == 'F' or Choise == '1':
        Choise = 'Forest'
    elif Choise.lower() == 'Desert' or Choise.lower() == 'D' or Choise == '2':
        Choise = 'Desert'
    elif Choise.lower() == 'House' or Choise.lower() == 'H' or Choise == '3':
        Choise = 'House'
    else:
        Choise = ''
time.sleep(2)
print('You have a weapon')
weaponchoosed = random.choice(Weapons)
print(weaponchoosed)
changerequest = input('Would you like to change weapons \n')
if changerequest == 'yes':
    weaponchoosed = random.choice(Weapons)
    print(weaponchoosed)
print('\nYou now in ' + Choise + ' and you have a weapon' + weaponchoosed)
time.sleep(1)
print('Now you see front of you')
if Choise == 'Forest':
    print(random.choice(Forest_Monsters))
if Choise == 'Desert':
    print(random.choice(Desert_Monsters))
if Choise == 'House':
    print(random.choice(House))
time.sleep(2)
PrintSleep('Use weapon to kill monster', 2)
print('You' + random.choice(Game_Result))
time.sleep(2)
print('Game Over')
