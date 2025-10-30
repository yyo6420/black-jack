from core.game_logic import calculate_hand_value, deal_two_each, dealer_play
from core.deck import build_standard_deck, shuffle_by_suit
from core.player_io import ask_player_action
player_1 = {"hand":[]} 
player_2 = {"hand":[]} 
cards = build_standard_deck()
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None: 
    cards = shuffle_by_suit(build_standard_deck())
    deal_two_each(cards,player_1,player_2)
    print(player["hand"])
    print(dealer["hand"])
    ask = ask_player_action()
    while ask == "H":
        player["hand"].append(deck.pop(0))
        print(player["hand"])
        calculate = calculate_hand_value(player["hand"])
        if calculate < 21:
            print("sorry, you pass 21 :(, don't worry maybe next time...")
            break
    dealer_turn = dealer_play(cards,dealer["hand"])
    if dealer_turn == True:
        player_1_score = calculate_hand_value(player["hand"])
        player_2_score = calculate_hand_value(dealer["hand"])
        if player_1_score < player_2_score:
            print("you win :)")
        elif player_2_score < player_1_score:
            print("sorry, you lost:(")
        else:
            print("we have a tie in points")
    else:
        print("you win :)")
if __name__=="__main":
    run_full_game(cards,player_1,player_2)