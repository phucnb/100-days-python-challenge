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
                try:
                    bet = int(input(f"Hey {players[player]['name']}, you have {players[player]['chips']} chips. How many chips you want to bet?: "))
                    if not 0 < bet <= players[player]['chips']:
                        print(f"Your bet should be from 0 to {players[player]['chips']}")
                    else:
                        bets = place_bet_for_player(players, player, bets, bet)
                        break
                except:
                    pass
        
        # draw cards for players
        drawn_cards = []
        for player in range(len(players)):
            # Draw 2 cards for each player
            drawn_cards.append([draw_card_from(deck), draw_card_from(deck)])
        dealer_cards = []
        dealer_cards.append([draw_card_from(deck)])
        
        # print players' cards 
        print_all_players_cards(drawn_cards)
        
        # Print Dealer's cards
        print("Dealer Card:", print_drawn_cards(dealer_cards, 0))
        input("Press any key to continue...")

        # Ask player to hit or stand
        points = {}  
        for player in range(len(players)):
            # If hand is Blackjack then move to the next player
            if is_blackjack(drawn_cards, player):
                print(f"Bingooo {players[player]['name']}, you have a Black Jack.")
                input("Press any key to continue...")
                points[player] = 0
            else:
                while True:
                    clear_screen()
                    points[player] = calculate_score(drawn_cards[player])
                    print(points[player])
                    print(f"Hey {players[player]['name']}")
                    print(f"Your cards are\033[95m{print_drawn_cards(drawn_cards, player)}\033[0m.")
                    print(f"Dealer's cards is\033[92m{print_drawn_cards(dealer_cards, 0)}\033[0m.")
                    # If hand score is >= 21 then won't allow player to hit another card
                    if calculate_score(drawn_cards[player]) >= 21:
                        input("Press any key to continue...")
                        break
                    # If player already hit 3 cards then won't allow player to hit another card
                    if len(drawn_cards[player]) == 5:
                        print("You can't hit anymore")
                        input("Press any key to continue...")
                        break
                    # Ask if player want to stand o hit
                    while True:
                        options = input("Do you want to hit (h) or stand (s): ").strip().lower()
                        if options in ['h', 's']:
                            break
                    # Draw a new card then break loop to start again.
                    if options == 'h':
                        hit(deck, drawn_cards, player)
                    else:
                        break
       
        input("Press any key to continue to reveal dealer card...")
        # Dealer deal second card
        dealer_cards[0].append(draw_card_from(deck))
        print(f"Dealer Cards:\033[92m{print_drawn_cards(dealer_cards, 0)}\033[0m")
        points['dealer'] = calculate_score(dealer_cards[0])
        if not (is_blackjack(dealer_cards, 0)):
            while calculate_score(dealer_cards[0]) < 17:
                dealer_cards[0].append(draw_card_from(deck))
                print(f"Dealer Cards:\033[92m{print_drawn_cards(dealer_cards, 0)}\033[0m")
                points['dealer'] = calculate_score(dealer_cards[0])
        else:
            points['dealer'] = 0
                
        
        # Compare hands
        for player in range(len(drawn_cards)):
            result = player_result(points['dealer'], points[player])
            if result == 'win':
                players[player]['chips'] += bets[player][1]*2
            elif result == 'push':
                players[player]['chips'] += bets[player][1]
            elif result == 'blackjack':
                players[player]['chips'] += bets[player][1]*2.5
            print(f"Player {player + 1} : {print_drawn_cards(drawn_cards, player)} => {result}")
            
            

                
            
            
            

        
        
        
            
        print_players(players)
        # continue to play or exit?
        while True:
            play_again = input("Do you want to continue to play? (y/n): ").strip()
            if play_again in ['y', 'n']:
                break
        if play_again == 'n':
            break
        clear_screen()
        
    

def player_result(dealer, player):
    if player == 0 and dealer != 0:
        return 'blackjack'
    elif player > 21 or (player < dealer and dealer < 22) or (player != 0 and dealer == 0):
        return 'lose'
    elif player == dealer:
        return 'push'
    else:
        return 'win'
    
    
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
        
        cards += f' \033[95m{card[0]}{card[1]}\033[0m'
        
    return cards

def points(points, player, point):
    '''The function update players' points as well as dealer and return the new points dict
    
    Parameters:
    ----------
        - points (dict): The points dict of all players
        - player (int): The index of the player in the list
        - point (str or int): point or 
    
    Returns:
    -------
        - dict: The points dict of all players
    '''
    points[player] = point
    return points

def print_all_players_cards(drawn_cards):
    for player_index, card in enumerate(drawn_cards):
        print(f"Player {player_index + 1}: ", end='')
        print(print_drawn_cards(drawn_cards, player_index))
        
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

def is_blackjack(drawn_card: list, player: int):
    '''This fuction checks if the player drawn cards is backjack then return True else False
    
    Parameters:
    ----------
        - drawn_cards (list): The list of all current drawn cards of all players
        - player (int): The index of the player in the list
    
    Returns:
    -------
        - Bool: True if the drawn cards are black jack, else then False
    ''' 
    if len(drawn_card[player]) != 2:
        return False
    
    
    if (drawn_card[player][0][0] == 'A' and drawn_card[player][1][0] in [10, 'J', 'Q', 'K', 'A']) or (drawn_card[player][1][0] == 'A' and drawn_card[player][0][0] in [10, 'J', 'Q', 'K', 'A']):
        return True
    else:
        return False
        
def calculate_score(cards: list):
    '''This fuction calculate the total score of a hand then return the score
    
    Parameters:
    ----------
        - cards (list): The list of all drawn cards of the player
    
    Returns:
    -------
        - int: total score for the hand
    '''
    
    total = 0
    ace = False
    for card in cards:
        if card[0] in ['J', 'Q', 'K']:
            total += 10
        elif card[0] == 'A':
            ace = True
            total += 11
        else:
            total += card[0]
    if ace and total > 21:
        total -= 10
    return total
            
        
    
if __name__ == "__main__":
    main()    