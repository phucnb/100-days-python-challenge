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
            # Draw 2 cards for each player
            drawn_cards.append([draw_card_from(deck), draw_card_from(deck)])
        dealer_cards = []
        dealer_cards.append([draw_card_from(deck)])
        
        # print players' cards 
        for player_index, card in enumerate(drawn_cards):
            print(f"Player {player_index + 1}: ", end='')
            print(print_drawn_cards(drawn_cards, player_index))
        
        # Print Dealer's cards
        print("Dealer Card:", print_drawn_cards(dealer_cards, 0))

        # Ask player to hit or stand
        for player in range(len(players)):
            while True:
                options = input(f"hey {players[player]['name']}, your cards is {print_drawn_cards(drawn_cards, player)}."\
                    "Do you want to hit (h) or stand (s): ").strip().lower()
                if options in ['h', 's']:
                    if options == 'h':
                        hit(deck, drawn_cards, player)
                    else:
                        print()
                        break
            
            
            
            

        
        
        
            
    
        # continue to play or exit?
        # play_again = input("Do you want to continue to play? (y/n): ").strip()
        # if play_again == 'n':
        #     break
        # clear_screen()
        
    print_players(players)
    
def print_drawn_cards(drawn_cards, player):
    '''This function print the drawn cards for a specific player
    
    Parameters:
    ----------
        - drawn_cards (list): The list of all drawn cards of all players
        - player (int): The index of the player in the list
    
    Returns:
    -------
        - str: The drawn cards of that player
    
    Examples:
    --------
    >>> print_drawn_cards(drawn_cards, 2)
    5♦ 4♦
    '''
    
    cards = ''
    for card in drawn_cards[player]:
        
        cards += f'{card[0]}{card[1]} '
        
    return cards
        
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
    '''Draw a random card from deck
    
    Parameters
    ----------
        deck (list): list of all cards in deck
    
    Return
    ------
        tuple: a tuple of 1 card
        
    Example
    -------
    >>> draw_card_from(deck)
    (7, '♠')
    ''' 
    
    drawn_card = random.sample(deck, 1)
    deck.remove(drawn_card[0])
    return drawn_card[0]
    
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
    
def hit(deck: list, drawn_cards: list, player: int):
    '''This function draws 1 more card for a player, add to drawn_cards list and return the list
    
    Parameters:
    ----------
        - deck (list): The list of all cards
        - drawn_cards (list): The list of all current drawn cards of all players
        - player (int): The index of the player in the list
    
    Returns:
    -------
        - list: The new drawn_cards list of all players
    '''
    
    new_card = draw_card_from(deck)
    
    drawn_cards[player].append(new_card)
    
    return drawn_cards
        
if __name__ == "__main__":
    main()    