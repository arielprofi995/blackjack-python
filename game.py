import random


RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
SUITS = {"pik": "♠", "kier": "♥", "karo": "♦", "trefl": "♣"}


def create_deck():
    """Create and shuffle a standard 52-card deck."""
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def draw_card(deck):
    """Remove and return the top card of the deck."""
    if not deck:
        raise ValueError("Talia jest pusta.")
    return deck.pop()


def deal_initial_hands(deck):
    """Deal two cards to each side, alternating between them."""
    if len(deck) < 4:
        raise ValueError("Do rozdania potrzebne są co najmniej cztery karty.")
    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player_hand.append(draw_card(deck))
        dealer_hand.append(draw_card(deck))
    return player_hand, dealer_hand


def hand_value(hand):
    """Calculate the highest valid total, reducing aces when needed."""
    total = 0
    aces = 0
    for rank, _ in hand:
        if rank == "A":
            total += 11
            aces += 1
        elif rank in ("J", "Q", "K"):
            total += 10
        else:
            total += int(rank)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def is_blackjack(hand):
    """Recognize a natural blackjack: exactly two cards worth 21."""
    return len(hand) == 2 and hand_value(hand) == 21


def play_dealer_turn(deck, dealer_hand):
    """Draw below 17 and stand on all totals of 17 or more."""
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))


def get_round_result(player_hand, dealer_hand):
    """Return the winner and a reason code for the completed round."""
    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    if player_total > 21:
        return "dealer", "player_bust"
    if dealer_total > 21:
        return "player", "dealer_bust"

    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack and dealer_blackjack:
        return "draw", "both_blackjack"
    if player_blackjack:
        return "player", "player_blackjack"
    if dealer_blackjack:
        return "dealer", "dealer_blackjack"

    if player_total > dealer_total:
        return "player", "player_higher"
    if dealer_total > player_total:
        return "dealer", "dealer_higher"
    return "draw", "equal"
