def calculate_hand_value(hand: list[dict]) -> int:
    hand_counter = 0
    for i in range(len(hand)):
        card = hand[i]
        try:
            number = int(card["rank"])
            hand_counter += number
        except:
            if card["rank"] == "J":
                hand_counter +=10
            elif card["rank"] == "Q":
                hand_counter +=10
            elif card["rank"] == "K":
                hand_counter +=10
            elif card["rank"] == "A":
                hand_counter +=1
    return hand_counter

def deal_two_each(cards_deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(cards_deck[0])
    cards_deck = cards_deck[1: ]
    dealer["hand"].append(cards_deck[0])
    cards_deck = cards_deck[1: ]
    player["hand"].append(cards_deck[0])
    cards_deck = cards_deck[1: ]
    dealer["hand"].append(cards_deck[0])
    cards_deck = cards_deck[1: ]
    return cards_deck

def dealer_play(cards_deck: list[dict], dealer: dict) -> bool:
    hand_value = calculate_hand_value(dealer["hand"])
    while hand_value <= 17:
        dealer["hand"].append(cards_deck[0])
        cards_deck = cards_deck[1: ]
        hand_value = calculate_hand_value(dealer["hand"])
        if (hand_value > 17 and hand_value <= 21):
            return True
        elif hand_value > 21:
            return False