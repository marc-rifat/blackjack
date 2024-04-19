import random

def create_deck():
    """Creates a deck of 52 cards"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Returns the value of a single card"""
    if card['value'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['value'] == 'Ace':
        return 11
    else:
        return int(card['value'])

def total_hand(hand):
    """Calculates the total value of a hand"""
    total = sum(card_value(card) for card in hand)
    # Adjust for Aces if total is over 21
    num_aces = sum(1 for card in hand if card['value'] == 'Ace')
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

def display_hand(hand, player):
    """Displays the hand of a player"""
    print(f"{player}'s hand:")
    for card in hand:
        print(f"{card['value']} of {card['suit']}")
    print("Total:", total_hand(hand))

def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player's turn
    while True:
        display_hand(player_hand, "Player")
        if total_hand(player_hand) > 21:
            print("Player busts! Dealer wins.")
            return
        action = input("Do you want to hit or stand? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        elif action == 'stand':
            break

    # Dealer's turn
    display_hand(dealer_hand, "Dealer")
    while total_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand, "Dealer")

    if total_hand(dealer_hand) > 21:
        print("Dealer busts! Player wins.")
    elif total_hand(player_hand) > total_hand(dealer_hand):
        print("Player wins!")
    elif total_hand(player_hand) < total_hand(dealer_hand):
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_blackjack()
