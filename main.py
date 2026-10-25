from game import (
    SUITS,
    create_deck,
    deal_initial_hands,
    draw_card,
    get_round_result,
    hand_value,
    is_blackjack,
    play_dealer_turn,
)


RESULT_MESSAGES = {
    "player": "Wygrywasz rundę!",
    "dealer": "Rundę wygrywa krupier.",
    "draw": "Remis!",
}
REASON_MESSAGES = {
    "player_bust": "Suma Twoich kart przekroczyła 21.",
    "dealer_bust": "Krupier przekroczył 21.",
    "both_blackjack": "Obie strony mają blackjacka.",
    "player_blackjack": "Masz blackjacka, czyli 21 z dwóch kart.",
    "dealer_blackjack": "Krupier ma blackjacka.",
    "player_higher": "Masz więcej punktów niż krupier.",
    "dealer_higher": "Krupier ma więcej punktów.",
    "equal": "Obie strony mają tyle samo punktów.",
}
STAT_KEYS = {"player": "wins", "dealer": "losses", "draw": "draws"}


def read_choice(prompt, choices):
    """Keep asking until the user selects an available action."""
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        print(f"Wybierz jedną z opcji: {', '.join(choices)}.")


def render_card(card, hidden=False):
    """Return seven text lines representing a visible or hidden card."""
    rank = "?" if hidden else card[0]
    symbol = "?" if hidden else SUITS[card[1]]
    return [
        "+-------+",
        f"|{rank:<2}     |",
        "|       |",
        f"|   {symbol}   |",
        "|       |",
        f"|     {rank:>2}|",
        "+-------+",
    ]


def show_hand(title, hand, hide_hole_card=False):
    """Display cards in rows of up to five without exposing a hidden total."""
    print(f"\n{title}")
    pictures = []
    for index, card in enumerate(hand):
        hidden = hide_hole_card and index == 1
        pictures.append(render_card(card, hidden))

    for start in range(0, len(pictures), 5):
        for line in zip(*pictures[start:start + 5]):
            print(" ".join(line))

    if hide_hole_card:
        print("Druga karta krupiera jest zakryta.")
    else:
        print(f"Punkty: {hand_value(hand)}")
        if is_blackjack(hand):
            print("Blackjack!")


def show_rules():
    """Explain the rules used by this version of the game."""
    print("\n=== ZASADY ===")
    print("Cel: uzyskać więcej punktów niż krupier, nie przekraczając 21.")
    print("Karty 2–10 mają wartość podaną na karcie.")
    print("J, Q i K są warte 10 punktów. As jest wart 1 lub 11.")
    print("Program dobiera wartość asa tak, aby uniknąć przekroczenia 21.")
    print("Blackjack to 21 z dwóch kart. Wygrywa ze zwykłym wynikiem 21.")
    print("Blackjack obu stron oznacza remis.")
    print("W swojej turze wybierasz: dobierz albo pas.")
    print("Krupier dobiera poniżej 17 i zatrzymuje się na 17 lub więcej.")
    print("Dotyczy to także miękkiego 17, np. asa i szóstki.")
    print("Każda runda rozpoczyna się nową, potasowaną talią 52 kart.")


def show_stats(stats):
    """Display results from completed rounds in the current session."""
    rounds = sum(stats.values())
    win_rate = 100 * stats["wins"] / rounds if rounds else 0
    print("\n=== STATYSTYKI SESJI ===")
    print(f"Ukończone rundy: {rounds}")
    print(f"Zwycięstwa: {stats['wins']}")
    print(f"Porażki: {stats['losses']}")
    print(f"Remisy: {stats['draws']}")
    print(f"Odsetek wygranych rund: {win_rate:.1f}%")


def play_round():
    """Play one complete round and return its winner."""
    deck = create_deck()
    player_hand, dealer_hand = deal_initial_hands(deck)

    print("\n=== NOWA RUNDA ===")
    show_hand("KRUPIER", dealer_hand, hide_hole_card=True)
    show_hand("TWOJE KARTY", player_hand)

    if not is_blackjack(player_hand) and not is_blackjack(dealer_hand):
        while hand_value(player_hand) < 21:
            choice = read_choice("\n1. Dobierz | 2. Pas: ", ("1", "2"))
            if choice == "2":
                break
            player_hand.append(draw_card(deck))
            show_hand("TWOJE KARTY", player_hand)

        if hand_value(player_hand) <= 21:
            play_dealer_turn(deck, dealer_hand)

    winner, reason = get_round_result(player_hand, dealer_hand)
    print("\n=== WYNIK RUNDY ===")
    show_hand("KRUPIER — ODKRYTE KARTY", dealer_hand)
    show_hand("TWOJE KARTY", player_hand)
    print(f"\n{RESULT_MESSAGES[winner]} {REASON_MESSAGES[reason]}")
    return winner


def main():
    """Run the menu, rounds, and session statistics."""
    stats = {"wins": 0, "losses": 0, "draws": 0}
    print("Witaj w Blackjacku!")

    try:
        while True:
            print("\n=== BLACKJACK ===")
            print("1. Zagraj rundę")
            print("2. Pokaż statystyki")
            print("3. Pokaż zasady")
            print("0. Zakończ")
            choice = read_choice("Wybierz opcję: ", ("1", "2", "3", "0"))

            if choice == "1":
                winner = play_round()
                stats[STAT_KEYS[winner]] += 1
            elif choice == "2":
                show_stats(stats)
            elif choice == "3":
                show_rules()
            else:
                break
    except (KeyboardInterrupt, EOFError):
        print("\nPrzerwano grę.")
    finally:
        show_stats(stats)
        print("\nDo zobaczenia!")


if __name__ == "__main__":
    main()
