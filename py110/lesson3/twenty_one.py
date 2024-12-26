import random
import os


def prompt(message: str) -> None:
    print(f"=> {message}")


def initialize_deck(empty: bool = False) -> dict[str, list[str]]:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "j",
        "q",
        "k",
        "a",
    ]
    if empty:
        return {suit: [] for suit in suits}
    return {suit: list(values) for suit in suits}


def get_hand_value(deck: dict[str, list[str]]) -> int:
    total_deck_value = 0
    total_aces = 0

    for value_list in deck.values():
        for value in value_list:
            if value in ("j", "q", "k"):
                total_deck_value += 10
            elif value == "a":
                total_aces += 1
                total_deck_value += 1
            else:
                total_deck_value += int(value)

    for _ in range(total_aces):
        if total_deck_value + 10 <= 21:
            total_deck_value += 10

    return total_deck_value


def is_busted(deck: dict[str, list[str]]) -> bool:
    return get_hand_value(deck) >= 21


def display_cards(
    dealer_deck: dict[str, list[str]],
    player_deck: dict[str, list[str]],
    dealer_hidden: bool = True,
) -> None:
    player_cards = []
    dealer_cards = []
    for value_list in player_deck.values():
        for element in value_list:
            match element:
                case "a":
                    player_cards.append("Ace")
                case "j":
                    player_cards.append("Jack")
                case "k":
                    player_cards.append("King")
                case "q":
                    player_cards.append("Queen")
                case _ as number:
                    player_cards.append(number)
    for value_list in dealer_deck.values():
        for element in value_list:
            match element:
                case "a":
                    dealer_cards.append("Ace")
                case "j":
                    dealer_cards.append("Jack")
                case "k":
                    dealer_cards.append("King")
                case "q":
                    dealer_cards.append("Queen")
                case _ as number:
                    dealer_cards.append(number)

    player_cards = " and ".join(sorted(player_cards))
    if not dealer_hidden:
        dealer_cards = " and ".join(sorted(dealer_cards))
        prompt(f"Dealer has: {dealer_cards}")
        prompt(f"Total Value: {get_hand_value(dealer_deck)}\n")
    else:
        prompt(f"Dealer has: {dealer_cards[0]} and unknown card\n")
    prompt(f"Player has: {player_cards}")
    prompt(f"Total value: {get_hand_value(player_deck)}\n")


def deal_random_cards(
    amount: int,
    previous_deck: dict[str, list[str]],
    target_deck: dict[str, list[str]],
) -> None:
    for _ in range(amount):
        random_suit = random.choice(list(previous_deck.keys()))
        random_value = random.choice(previous_deck[random_suit])

        previous_deck[random_suit].remove(random_value)
        target_deck.setdefault(random_suit, []).append(random_value)


def clear_terminal() -> None:
    os.system("clear")


def ask_user() -> str:
    while True:
        prompt("Would you like to hit or stay?")
        choice = input().strip().lower()
        if choice in ("hit", "stay"):
            break
        prompt('Sorry please enter either "hit" or "stay".')
    return choice


def calculate_winner(
    player_deck: dict[str, list[str]], dealer_deck: dict[str, list[str]]
) -> str:
    player_deck_value = get_hand_value(player_deck)
    dealer_deck_value = get_hand_value(dealer_deck)

    if player_deck_value > dealer_deck_value:
        return "player"
    if dealer_deck_value > player_deck_value:
        return "dealer"
    return "tie"


def main() -> None:
    clear_terminal()

    winner = None
    global_deck = initialize_deck()
    player_deck = initialize_deck(empty=True)
    dealer_deck = initialize_deck(empty=True)

    deal_random_cards(2, global_deck, dealer_deck)
    deal_random_cards(2, global_deck, player_deck)

    while True:
        clear_terminal()
        display_cards(dealer_deck, player_deck)
        decision = ask_user()
        if decision == "stay":
            break
        deal_random_cards(1, global_deck, player_deck)
        if is_busted(player_deck):
            winner = "computer"
            break

    while winner != "computer":
        clear_terminal()
        display_cards(dealer_deck, player_deck)
        if get_hand_value(dealer_deck) >= 17:
            break
        deal_random_cards(1, global_deck, dealer_deck)
        if is_busted(dealer_deck):
            winner = "player"
            break

    clear_terminal()
    display_cards(dealer_deck, player_deck, dealer_hidden=False)

    if winner is None:
        winner = calculate_winner(player_deck, dealer_deck)
    match winner:
        case "player":
            prompt("Congrats for winning!")
        case "computer":
            prompt("Oof computer won. Better luck next time")
        case _:
            prompt("It's a tie!")


main()
