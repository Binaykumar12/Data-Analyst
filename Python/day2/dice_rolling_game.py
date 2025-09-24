import random

count=0
number_of_dice = int(input("Enter the number of dice you want to roll: "))
while True:
    answer = input("Roll the dice? (y/n): ").lower()
    dice = [0]*number_of_dice
    if answer == 'y':
        for i in range(number_of_dice):
         dice[i] = random.randint(1, 6)
        count+=1
        print(f"Dice :{dice} , Number of times dice enrolled {count}")
        
    elif answer == 'n':
        print("Thanks for playing!!")
        break
    else:
        print("Invalid Choice!")
