import random

computers_guess = random.randint(1, 100)

while True:
  try:
   guess = int(input("Guess the number between 1 and 100 : "))
   if 1<=guess<=100 :
    if guess==computers_guess:
        print("Congratulations!! You guessed the right number.")
        break
    
    elif guess>computers_guess:
        print("Too High!")
    else:
        print("Too Low !")
   else:
      print("Invalid choice !!")
  except ValueError:
      print("Enter a valid number ! ")
      continue
      
 






# import random

# computers_guess = random.randint(1, 100)

# while True:
#   guess_str = input("Guess the number between 1 and 100 : ")
  
#   if not guess_str.isdigit():
#    print("Please enter a valid number : ")
#    continue

#   guess = int(guess_str)
  
#   if 1<=guess<=100 :
#     if guess==computers_guess:
#         print("Congratulations!! You guessed the right number.")
#         break
    
#     elif guess>computers_guess:
#         print("Too High!")
#     else:
#         print("Too Low !")
#   else:
#       print("Invalid choice !!")





