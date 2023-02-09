import random
from art import *
import os # to clear screen

DEFAULT_CHIPS = 100

def main():
    clear_screen()
    # Initial deck
    deck = shuffle_deck()
    
    # Initial number of player
    players = []
    while True:
        if players := initial_players(int(input("How many players?: ")), players):
            break
        else: 
            print("Number of player should be from 1 to 7")
    print_players(players)
    
    while True:
        # place bets for players
        bets = []
        for player in range(len(players)):
            while True:
                bet = int(input(f"Hey {players[player]['name']}, you have {players[player]['chips']} chips. How many chips you want to bet?: "))
                if not 0 < bet <= players[player]['chips']:
                    print(f"Your bet should be from 0 to {players[player]['chips']}")
                else:
                    bets = place_bet_for_player(players, player, bets, bet)
                    break
        
        # draw cards for players
        drawn_cards = []
        for player in range(len(players)):
            cards = [draw_card_from(deck), draw_card_from(deck)]
            drawn_cards.append(cards)
        
        drawn_cards[0].append(draw_card_from(deck))
        drawn_cards[1].append(draw_card_from(deck))
        drawn_cards[2].append(draw_card_from(deck))
        print(drawn_cards)
        print_drawn_cards(drawn_cards)
        
        
    
        # continue to play or exit?
        play_again = input("Do you want to continue to play? (y/n): ").strip()
        if play_again == 'n':
            break
        clear_screen()
        
    print_players(players)
    
def print_drawn_cards(drawn_cards):
    for player in range(len(drawn_cards)):
        print(f"Player {player + 1}: ", end='')
        for card in drawn_cards[player]:
            # print(type(card))
            # print(card)
            print(f'{card[0][0]}{card[0][1]} ', end='')
        print()
        
def initial_players(number_of_players, players):
    '''
    The function initial list of players with name and 100 chips
    if 0 < number_of_players < 8 then return lists of players, else return empty list
    '''
    if 0 < number_of_players < 8:  
        for player in range(number_of_players):
            players.append({'name' : f'Player {player + 1}', 'chips' : DEFAULT_CHIPS})
    return players
    
def draw_card_from(deck):
    '''
    The function draw 1 random card and return the card with type of LIST.
    The function also remove the drawn card from the deck.
    Parameters: The function takes 1 parameter
    - deck: LIST of all cards
    Return: The function returns the drawn card in LIST
    ''' 
    drawn_card = random.sample(deck, 1)
    deck.remove(drawn_card[0])
    return drawn_card
    
def update_chips_for(players, player, chips):
    '''
    The function update chip for a specific player in players list
    player and chips should be and int
    Parameters: The function takes 3 parameters
    - players: LIST of all players
    - player: INT index of the player in players list
    - chips: INT amount of chip want to update
    '''
    players[player]['chips'] += chips  

def place_bet_for_player(players, player, bets, bet):
   '''
   The function updates chips for a specific player in players list
   And update bets list
   Parameters: the function takes 4 parameters
   - players: LIST of players
   - player: INT index of the player in players list
   - bets: LIST of bets of all players
   - bet: INT amount of chip which player want to bet
   Return: The function return a updated bets LIST
   '''
   update_chips_for(players, player, -bet)
   bets.append([player, bet])
   return bets

def print_players(players):
    '''
    The function print all players with their name and chips
    Parameters: the function takes 1 parameter
    - players: LIST of all players
    '''
    for player in players:
        print(f"{player['name']} has {player['chips']} chip(s).")

def shuffle_deck():
    '''
    The function reset the number of card in deck to 52 cards
    and return deck is the list of 52 unique cards
    '''
    deck = [(rank, suit) for rank in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
            for suit in ['♥', '♦', '♠', '♣']]  
    return deck

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
if __name__ == "__main__":
    main()    