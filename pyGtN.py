import random
import sys
from os import system
from ascii import top, breaker, welcome, rule_txt, about_txt
system('title '+ 'Guess the Number')


# DIFFICULTY:
easy = random.randint(1, 10)
medium = random.randint(1, 100)
hard = random.randint(-500, 500)
chances = 0

# functions
def replay():
    '''asking the player whether they want to play the game again or not'''
    print(breaker)
    print('type "m" to go back to main menu')
    ans = input('do you want to play again? (y/n)\n> ')[:1].lower()
    if ans == 'y':
        game()
    elif ans == 'n':
        sys.exit()
    elif ans == 'm':
        menu()
    else:
        print('>> error: unrecognized command.')
        replay()

def process(guess, num, chances):
    '''see if the number the player entered is correct. if not, remove one chance from the player.'''
    if guess > num:
        print('the number you guessed is too high.')
        return chances - 1
    elif guess < num:
        print('the number you guessed is too low.')
        return chances - 1
    else:
        print(f'you got it! The answer was "{num}".')
        replay()

def difficulty():
    '''selecting difficulty levels.'''
    print('difficulty: easy = 1 to 10, medium = 1 to 100, hard = -500 to 500')
    diff = input('choose difficulty:\n> ').lower()
    global chances
    if diff == 'easy':
        chances = 5
        print('im thinking of a number between 1 and 10.')
        return easy
    elif diff == 'medium':
        chances = 7
        print('im thinking of a number between 1 and 100.')
        return medium
    elif diff == 'hard':
        chances = 10
        print('im thinking of a number between -500 and 500.')
        return hard
    else:
        print('>> error: unrecognized command.')
        difficulty()

def game():
    '''plays the game'''
    print(welcome)
    num = difficulty()
    global chances
    # hack, i guess. print(f'num: {num}')
    guess = 0

    while guess != num:
        print(breaker)
        print(f'you have {chances} chances left to guess the correct number.')
        # im using try to catch the errors from input (entering the letters instead of numbers for example.)
        # i didnt wanna write some other long stuff.
        try:
            guess = int(input('enter your guess:\n> '))
            chances = process(guess, num, chances)
            if chances == 0:
                print(f'{breaker}\nyou\'ve ran out of guesses, you lose.')
                print(f'the number was "{num}"')
                return
            elif guess != num:
                print('wrong! guess again.')
        except:
            print(">> error: numbers only.")

def menu():
    '''main menu of the game.'''
    print(top)
    menu = True
    while menu:
        opt = input("choose menu:\n> ")[:1].lower()
        if opt == 'p':
            game()
        elif opt == 'r':
            print(rule_txt)
        elif opt == 'a':
            print(about_txt)
        elif opt == 'q':
            sys.exit()
        else:
            print('>> error: unrecognized command.')
            menu = True
# starting game
menu()



