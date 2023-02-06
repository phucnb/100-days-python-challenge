from art import *
import os # to clear screen

def main():
    clear_screen()
    print(text2art("The Secret Auction",font='rnd-small',chr_ignore=True))
    print("Welcome to The Secret Auction.")
    bidders = {}

    while True:
        '''
        the loop will continue to prompt for name and bid until say 'no'
        '''
        name = input("What is your name: ")
        while True:
            # Try-except to catch invalid interger input
            try:
                bid = int(input("What is your bid: $"))
                break
            except:
                pass
        
        # Add new bidder to dict
        bidders[name] = bid
        
        # Ask if want to add more bidders
        while True:
            more_bid = input("Are there any other bidders: Type 'yes' or 'no'\n").lower()
            if more_bid in ['yes','no']:
                break
        
        if more_bid == 'no':
            break
        # clear_screen()

    # Find the highest bidders
    highest_bidders = find_highest_bidders(bidders)
    
    while len(highest_bidders) > 1:
        '''
        The while loop will continue until there is only 1 bidder in the dict
        next(iter(highest_bidders.values() => print the VALUE of the first element in dict
        next(iter(highest_bidders.keys() => print the KEY of the first element in dict
        '''
        
        print(f"There are {len(highest_bidders)} bidders have the same bid at : ${next(iter(highest_bidders.values()))}")
        print("Therefore we will have another round for those bidders.")
        # loop all the bidders to ask for their bid
        for bidder in highest_bidders:
            while True:
                try:
                    highest_bidders[bidder] = int(input(f"Hey {bidder}, what is your bid: $"))
                    break
                except:
                    pass
        
        # find highest bidders again
        highest_bidders = find_highest_bidders(highest_bidders)    

    print(f"The winner is {next(iter(highest_bidders.keys()))} with a bid of ${next(iter(highest_bidders.values()))}.")    


def find_highest_bidders(bidders):
    '''
    The function take 1 parameter as a dict of all bidders
    and return a dict bidders have the same highest bid
    '''
    highest_bid = 0
    highest_bidders = {}
    for bidder in bidders:
        highest_bid = bidders[bidder] if bidders[bidder] > highest_bid else highest_bid
        
    for bidder in bidders:
        if bidders[bidder] == highest_bid:
            highest_bidders[bidder] = bidders[bidder]
        
    return highest_bidders

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
        
if __name__ == "__main__":
    main()