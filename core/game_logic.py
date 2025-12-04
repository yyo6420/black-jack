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

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None: 
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    return None

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer) < 17:
        dealer["hand"].append(deck.pop(0))
        if calculate_hand_value(dealer) > 17 and calculate_hand_value(dealer) < 50:
            return True
        elif calculate_hand_value(dealer) > 50:
            return False