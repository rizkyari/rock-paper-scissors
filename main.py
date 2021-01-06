import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = input("Choose your weapon: rock, paper, or scissors?\n")
weapons = ["rock", "paper", "scissors"]
pc = random.choice(weapons)

if user == "rock" and pc == "rock":
  print(f"You choose {rock} and pc choose {rock}\nDraw")
elif user == "rock" and pc == "paper":
  print(f"You choose {rock} and pc choose {paper}\nYou Lose")  
elif user == "rock" and pc == "scissors":
  print(f"You choose {rock} and pc choose {scissors}\nYou Win")  
elif user == "paper" and pc == "rock":
  print(f"You choose {paper} and pc choose {rock}\nYou Win")
elif user == "paper" and pc == "paper":
  print(f"You choose {paper} and pc choose {paper}\nDraw")  
elif user == "paper" and pc == "scissors":
  print(f"You choose {paper} and pc choose {scissors}\nYou Lose")   
elif user == "scissors" and pc == "rock":
  print(f"You choose {scissors} and pc choose {rock}\nYou Lose")
elif user == "scissors" and pc == "paper":
  print(f"You choose {scissors} and pc choose {paper}\nYou Win")  
elif user == "scissors" and pc == "scissors":
  print(f"You choose {scissors} and pc choose {scissors}\nDraw")   
else:
  print("Only rock, paper, or scissors is allowed!!!")  