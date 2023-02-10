import art, game_data
import os, random

def main():
    
    
    account_a = pick_random_account(game_data.data)
    account_b = pick_random_account(game_data.data)
    while account_a == account_b:
        account_b = pick_random_account(game_data.data)
        
    score = 0
    while True:
        clear_screen()
        print(art.logo)
        if score > 0:
            print("You are right! Current score: ", score)
        print(f"Compare A: {print_account(account_a)}")    
        print(art.vs)
        print(f"Against B: {print_account(account_b)}")
        while True:
            guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            if guess in ['A', 'B']:
                break
        
        if guess == who_has_more(account_a, account_b):
            score += 1
            # game_data.data.remove(account_a)
            account_a = account_b
            account_b = pick_random_account(game_data.data)
            while account_a == account_b:
                account_b = pick_random_account(game_data.data)
        else:
            print("Sorry, that's wrong. Final Score: ", score)
            break
        
    
def who_has_more(account_a, account_b):
    if account_a['follower_count'] > account_b['follower_count']:
        return "A"
    else:
        return "B"
    
def print_account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def pick_random_account(data):
    return random.choice(data)

def clear_screen():
    '''
    The function clears the terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == "__main__":
    main()