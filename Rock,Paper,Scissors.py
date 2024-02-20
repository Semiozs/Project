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

decision = (input("What you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))

number_index = int(decision[0]) -1

robot_decision = random.randint(0,3)

if number_index ==  robot_decision:
    print(f"It's a draw{int(number_index), int(robot_decision)}")
if number_index == 0 and robot_decision == 1:
    print(f"You lose{int(number_index), int(robot_decision)}")
if number_index == 0 and robot_decision == 2:
    print(f"You win{int(number_index), int(robot_decision)}")