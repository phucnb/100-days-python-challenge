from main import shuffle_deck, initial_players, update_chips_for, place_bet_for_player, draw_card_from, print_drawn_cards, hit, is_blackjack
import random

def test_shuffle_deck():
        deck = shuffle_deck()
        assert len(deck) == 52 # Test total cards in deck. Should be 52 cards
        assert len(set(deck)) == len(deck) # Test all cards are unique
        
        # Test ranks and suites for each card
        for card in deck:
            assert card[0] in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
            assert card[1] in ['♥', '♦', '♠', '♣']
        
def test_initial_players():
    players = []
    # Test invalid number of players
    assert len(initial_players(8, [])) == 0
    assert len(initial_players(0, [])) == 0
    assert len(initial_players(-1, [])) == 0
    assert len(initial_players(9, [])) == 0
    
    # Test valid number of players
    assert len(initial_players(1, [])) == 1
    assert len(initial_players(7, [])) == 7
    assert len(initial_players(5, [])) == 5
    
    # Test name and chips
    players = initial_players(5, [])
    for player in range(len(players)):
        assert players[player]['name'] == f'Player {player + 1}'
        assert players[player]['chips'] == 100
 
def test_update_chips_for():
    players = []
    players = initial_players(2, players)
    update_chips_for(players, 0, -50)
    update_chips_for(players, 1, 10)
    assert players[0]['chips'] == 50
    assert players[1]['chips'] == 110
     
def test_place_bet_for_player():
    players = initial_players(random.randint(1, 7), [])    
    bets = []
    for player in range(len(players)):
        bet = random.randint(1, 100)
        bets = place_bet_for_player(players, player, bets, bet)
        assert len(bets) == player + 1
        assert players[player]['chips'] == 100 - bets[player][1]
        
def test_draw_card_from():
    deck = shuffle_deck()
    
    assert isinstance(draw_card_from(deck), tuple)
    assert len(draw_card_from(deck)) == 2
    assert len(deck) == 50

def test_print_drawn_cards():
    deck = shuffle_deck()
    drawn_card = []
    drawn_card.append([draw_card_from(deck)])
    assert print_drawn_cards(drawn_card, 0) == f'{drawn_card[0][0][0]}{drawn_card[0][0][1]} '
    
def test_hit():
    deck = shuffle_deck()
    drawn_card = []
    drawn_card.append([draw_card_from(deck)])
    assert len(drawn_card[0]) == 1
    drawn_card = hit(deck, drawn_card,0)
    assert len(drawn_card[0]) == 2
    drawn_card = hit(deck, drawn_card,0)
    assert len(drawn_card[0]) == 3

def test_is_blackjack():
    drawn_card = [[('A', '♥'),('J', '♥')],[('A', '♥'),('J', '♥'),('J', '♥')],[('J', '♥'),('J', '♥')],[('K', '♥'),('A', '♥')],]
    assert is_blackjack(drawn_card, 0) == True
    assert is_blackjack(drawn_card, 1) == False
    assert is_blackjack(drawn_card, 2) == False
    assert is_blackjack(drawn_card, 3) == True

    
    