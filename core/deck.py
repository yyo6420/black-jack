import random
def build_standard_deck() -> list[dict]: 
    cards_deck=[]
    card_details = {"rank":None,"suite":None}
    for card in  [i for i in range(2,11)] + ["J", "Q", "K", "A"]:
        for suite in ["H","C","D","S"]:
            card_details = {"rank": str(card), "suite": suite}
            cards_deck.append(card_details)
    return cards_deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]: 
    for swap in range(swaps):
        first_card = random.choice(deck)
        second_card = random.choice(deck)
        if first_card != second_card:
            if first_card["suite"] == "H":
                while second_card%5!=0:
                    second_card = random.choice(deck)
                    if second_card %5==0:
                        break
            elif first_card["suite"] == "C":
                while second_card%3!=0:
                    second_card = random.choice(deck)
                    if second_card %3==0:
                        break
            elif first_card["suite"] == "D":
                while second_card%2!=0:
                    second_card = random.choice(deck)
                    if second_card %2==0:
                        break
            elif first_card["suite"] == "S":
                while second_card%7!=0:
                    second_card = random.choice(deck)
                    if second_card %7==0:
                        break
                