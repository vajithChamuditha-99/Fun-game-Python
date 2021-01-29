import time
import random
def display_intro():
    a='''You are in the Kindom of Dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is hungry and will eat you on sight.'''
    print(a)

def choose_cave():
    cave='' #local variable with empty string
    while cave!='1' and cave!='2' and cave!='3' and cave!='4':
        print('Which cave will you go into?(1 or 2 or 3 or 4)')
        cave=input()
    return cave

def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you!')
    print('He opens his jaws and...')
    time.sleep(2)
    friendlycave = random.randint(1, 3)
    print(cave_number)
    if cave_number==friendlycave:
        print('Give you his treasure!')
    else:
        print('Gobbles you down!')
play_again='y'
while play_again=='y':   
    display_intro()
    cave_number=choose_cave()
    check_cave(cave_number)
    print('Do you want to play again?? \n press y if you need to exit press n')
    play_again=input()
    if play_again=='y':
        print('you can try again')
    else:
        play_again=='n'
print('End the game')
