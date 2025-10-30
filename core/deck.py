import random
def build_standard_deck() -> list[dict]: 
    cards_deck=[]
    card_details = {"rank":None,"suit":None}
    for card in  [i for i in range(2,11)] + ["J", "Q", "K", "A"]:
        for suite in ["H","C","D","S"]:
            card_details = {"rank": str(card), "suit": suite}
            cards_deck.append(card_details)
    return cards_deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]: 
    for swap in range(swaps):
        first_card_index = random.randint(0,51)
        first_card =  deck[first_card_index]
        second_card_index = random.randint(0,51)
        second_card =  deck[second_card_index]
        if first_card_index != second_card_index:
            if first_card["suit"] == "H":
                while second_card_index%5!=0:
                    second_card_index = random.randint(0,51)
                    second_card = deck[second_card_index]
                    if second_card_index%5==0:
                        break
            elif first_card["suit"] == "C":
                while second_card_index%3!=0:
                    second_card_index = random.randint(0,51)
                    second_card = deck[second_card_index]
                    if second_card_index%3==0:
                        break
            elif first_card["suit"] == "D":
                while second_card_index%2!=0:
                    second_card_index = random.randint(0,51)
                    second_card = deck[second_card_index]
                    if second_card_index%2==0:
                        break
            elif first_card["suit"] == "S":
                while second_card_index%7!=0:
                    second_card_index = random.randint(0,51)
                    second_card = deck[second_card_index]
                    if second_card_index%7==0:
                        break
        deck[first_card_index],deck[second_card_index] = deck[second_card_index],deck[first_card_index]    
    return deck

print(shuffle_by_suit(build_standard_deck()))