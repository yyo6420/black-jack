def ask_player_action() -> str:
    options = ("H", "h", "S", "s")
    answer = input("what would you like to do?")
    while answer not in options:
        print("Invalid key")
        answer = input("what would you like to do?")
        if answer in options:
            return answer
    return answer