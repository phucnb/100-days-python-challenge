import random
from art import *

deck = [(rank, suit) for rank in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
            for suit in ['♥', '♦', '♠', '♣']]
players = []
DEFAULT_CHIPS = 100

def main():
    number_of_players = int(input("How many players: "))
    # Initial Name and chips at the beginning
    for player in range(number_of_players):
        players.append({'name' : f'Player {player + 1}', 'chips' :  DEFAULT_CHIPS})
    
    place_bet_for_players()
    
    
    # for player in range(number_of_players):
    #     bets.append(int(input(f"How much you going to bet Player {player}: ")))
    # for player in range(number_of_players):
    #     card = draw_card_from(deck)
    #     players.append({'player' : player + 1, 'cards' : card, 'chips' : 100 - bets[player]})
    # for player in players:
    #     print(player)
    
def draw_card_from(deck):    
    drawn_cards = random.sample(deck, 2)
    for card in drawn_cards:
        deck.remove(card)
    return drawn_cards
    
def update_chips_for(player, amount):
    # bet = (int(input(f"You have {players[player]('chips')} chips. How much you going to bet Player {player + 1}: ")))
    players[player]['chips'] += amount  

def place_bet_for_players():
    for player in range(len(players)):
        bet = (int(input(f"You have {players[player]['chips']} chips. How much you going to bet {players[player]['name']}: ")))
        update_chips_for(player, -bet)

def print_players():
    print(f"{player['name']} has {player['chips']} chip(s).")

def update_players():    
    for player in range(len(players)):
        if player[player]['chips'] < 0:
            players.remove(player)

        

if __name__ == "__main__":
    main()    