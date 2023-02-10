import random
EASY = 10
HARD = 5

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thingking of a number between 1 and 100.")

    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if level in ['easy', 'hard']:
            break
    
    attempt = EASY if level == 'easy' else HARD
    number = random.randint(1, 100)
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number")
        while True:
            try:
                guess = int(input("Make a guess: "))
                break
            except:
                pass
        if guess == number:
            print("You got it! The answer was", number)
            break
        elif guess > number:
            print('Too high.')
        else:
            print('Too low.')
        print("Guess again.")
        attempt -= 1
        
if __name__ == "__main__":
    main()

    
    
        
        
        