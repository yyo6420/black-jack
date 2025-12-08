from core.game_logic import calculate_hand_value, deal_two_each, dealer_play
from core.deck import build_standard_deck, shuffle_by_suit
from core.player_io import ask_player_action
player_1 = {"hand": list()} 
player_2 = {"hand": list()} 
def run_full_game(player: dict, dealer: dict) -> None: 
    cards = shuffle_by_suit(build_standard_deck())
    cards = deal_two_each(cards,player_1,player_2)
    print(player["hand"])
    print(dealer["hand"])
    lost = False
    options = ("H", "h")
    print("here is your options:\nh : hit a card\ns: skip the turn")
    while ask_player_action() in options:
        player["hand"].append(cards.pop(0))
        print(player["hand"])
        calculate = calculate_hand_value(player["hand"])
        if calculate > 21:
            print("sorry, you pass 21 :(\ndon't worry maybe next time...")
            lost = True
            break
    if lost == True:
        return False
    dealer_turn = dealer_play(cards,dealer)
    print(dealer["hand"])
    if dealer_turn:
        player_1_score = calculate_hand_value(player["hand"])
        player_2_score = calculate_hand_value(dealer["hand"])
        print(player_1_score)
        print(player_2_score)
        if player_1_score < player_2_score:
            print("you win :)")
        elif player_2_score < player_1_score:
            print("sorry, you lost:(")
        else:
            print("we have a tie in points")
    else:
        player_1_score = calculate_hand_value(player["hand"])
        player_2_score = calculate_hand_value(dealer["hand"])
        print(player_1_score)
        print(player_2_score)
        print("you win :)")
        return True
if __name__=="__main__":
    run_full_game(player_1,player_2)