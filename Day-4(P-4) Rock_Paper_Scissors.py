import random

user_choice = int(input("Enter your choice: 0 - rock 1 - paper 2 - scissors. "))
print(f"You chose {user_choice}")
comp_choice = random.randint(0,2)
print(f"Computer chose {comp_choice}")
if(user_choice == 0 and comp_choice == 2):
    print("You Won!!")
elif(user_choice == 0 and comp_choice == 2):
    print("You Lose!!")
elif(comp_choice > user_choice):
    print("You Lose!!")
elif(user_choice > comp_choice):
    print("You Won!!")
elif(user_choice == comp_choice):
    print("It's a TIE")
else:
    print("INVALID CHOICE!!")

