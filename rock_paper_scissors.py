import random


choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print("You chose")
if choice==0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif choice==1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif choice==2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
else:
    print("Invalid input")
    exit(0)
computer_choice=random.randint(0,2)
print("Computer Chose")
if computer_choice==0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_choice==1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif computer_choice==2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
if choice==0 and computer_choice==0:
    print("Draw")
elif choice==0 and computer_choice==1:
    print("You Lose")
elif choice==0 and computer_choice==2:
    print("You Win")
elif choice==1 and computer_choice==0:
    print("You Win")
elif choice==1 and computer_choice==1:
    print("Draw")
elif choice==1 and computer_choice==2:
    print("You Lose")
elif choice==2 and computer_choice==0:
    print("You Lose")
elif choice==2 and computer_choice==1:
    print("You Win")
elif choice==2 & computer_choice==2:
    print("Draw")



