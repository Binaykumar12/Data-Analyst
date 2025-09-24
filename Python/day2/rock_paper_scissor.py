import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

symbols = {ROCK: '🪨',
           PAPER: '📝',
           SCISSORS: '✂️'
           }
choices = tuple(symbols.keys())

while True:
    computer_guess = random.choice(choices)

    user_input = input("Rock ,Paper ,Scissor (r,p,s) : ").lower()

    if user_input in choices:
        if (user_input == computer_guess):
            print(f"You choose {symbols[user_input]}")
            print(f"Computer choose {symbols[computer_guess]}")
            print("Draw")

        elif (user_input == ROCK and computer_guess == SCISSORS) or \
            (user_input == SCISSORS and computer_guess == PAPER) or \
                (user_input == PAPER and computer_guess == ROCK):
            print(f"You choose {symbols[user_input]}")
            print(f"Computer choose {symbols[computer_guess]}")
            print("You Win!")
            
            while True:

                again = input("Continue (y/n) : ").lower()            
                if again == 'y':
                    break

                elif again == 'n':
                    print("Thanks for Playing !!")
                    exit()
                else:
                    print("Invalid Choice ! Please Select (y/n): ")

        else:
            print(f"You choose {symbols[user_input]}")
            print(f"Computer choose {symbols[computer_guess]}")
            print("You Lose !!")

    else:
        print("Invalid Choice !!")
