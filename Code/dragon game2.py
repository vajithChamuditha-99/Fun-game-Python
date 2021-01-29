import random
import time


def display_intro():
    a='''You are in the Kingdom of Dragons.In front of you,
you see two caves.In one cave, the dragon is friendly
and will share his treasure with you.The other dragon
is hungry and will eat you on sight.'''
    print(a)
    
def intro():
    display_intro()



def choose_cave():
    cave = '' # local variable with empty string
    while cave != '1' and cave != '2' and cave!='3' and cave!='4':
        print()
        print('Which cave will you go into? (1 or 2 or 3 or 4):')
        cave = input()
    return cave

def check_cave():
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ')
    print('He opens his jaws and...')
    time.sleep(2)
    
   
def main():
    friendlyCave =random.randint(1,3)
    intro()
    cave_number = choose_cave()
    check_cave()

    if int(cave_number) == friendlyCave:
        print()
        print ('Gives you his treasure')
    else:
        print()
        print("Gobbles you down!")
        print()
    p=str(input('If you want to play again Press y\nIf you need to exit press n\n'))
    print()
    if p=='y':
        main()
    else:
        quit()

    
main()
