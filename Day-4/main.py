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
rps = {
    0: rock,
    1: paper,
    2: scissors
}
while True:
    while True:
        try:
            select = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if select in [0, 1, 2]:
                break
        except:
            pass
    print(rps[select])
    computer = random.choice(list(rps.keys()))
    print("Computer choose:")
    print(rps[computer])
    if (select - computer) in [-1, 2]:
        print("You lost")
    elif (select - computer) == 0:
        print("It's a draw")
    else:
        print("You win")

    again = input("Enter y/yes to play again or enter anything else to exit: ").lower().strip()
    if again in ['y', 'yes']:
        pass
    else:
        break