"""
My first attempt at programming a noughts
and crosses game using MM
J-A-Collins 04-03-2022
"""
# Imports
import time

# # # Player icons
player = "X"
ai = "0"
# # # An empty dictionary for the game board
game_board = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}


def check_for_winner() -> bool:
    """Checks for a game winner"""
    # # # Row one validation:
    if (
        game_board[1] == game_board[2]
        and game_board[1] == game_board[3]
        and game_board[1] != " "
    ):
        return True
    # # # Row two validation:
    elif (
        game_board[4] == game_board[5]
        and game_board[4] == game_board[6]
        and game_board[4] != " "
    ):
        return True
    # # # Row three validation:
    elif (
        game_board[7] == game_board[8]
        and game_board[7] == game_board[9]
        and game_board[7] != " "
    ):
        return True
    # # # Column one validation:
    elif (
        game_board[1] == game_board[4]
        and game_board[1] == game_board[7]
        and game_board[1] != " "
    ):
        return True
    # # # Column two validation:
    elif (
        game_board[2] == game_board[5]
        and game_board[2] == game_board[8]
        and game_board[2] != " "
    ):
        return True
    # # # Column three validation:
    elif (
        game_board[3] == game_board[6]
        and game_board[3] == game_board[9]
        and game_board[3] != " "
    ):
        return True
    # # # Diagonal one validation:
    elif (
        game_board[1] == game_board[5]
        and game_board[1] == game_board[9]
        and game_board[1] != " "
    ):
        return True
    # # # Diagonal two validation:
    elif (
        game_board[7] == game_board[5]
        and game_board[7] == game_board[3]
        and game_board[7] != " "
    ):
        return True
    else:
        return False


def check_who_won(icon):
    if (
        game_board[1] == game_board[2]
        and game_board[1] == game_board[3]
        and game_board[1] == icon
    ):
        return True
    # # # Row two validation:
    elif (
        game_board[4] == game_board[5]
        and game_board[4] == game_board[6]
        and game_board[4] == icon
    ):
        return True
    # # # Row three validation:
    elif (
        game_board[7] == game_board[8]
        and game_board[7] == game_board[9]
        and game_board[7] == icon
    ):
        return True
    # # # Column one validation:
    elif (
        game_board[1] == game_board[4]
        and game_board[1] == game_board[7]
        and game_board[1] == icon
    ):
        return True
    # # # Column two validation:
    elif (
        game_board[2] == game_board[5]
        and game_board[2] == game_board[8]
        and game_board[2] == icon
    ):
        return True
    # # # Column three validation:
    elif (
        game_board[3] == game_board[6]
        and game_board[3] == game_board[9]
        and game_board[3] == icon
    ):
        return True
    # # # Diagonal one validation:
    elif (
        game_board[1] == game_board[5]
        and game_board[1] == game_board[9]
        and game_board[1] == icon
    ):
        return True
    # # # Diagonal two validation:
    elif (
        game_board[7] == game_board[5]
        and game_board[7] == game_board[3]
        and game_board[7] == icon
    ):
        return True
    else:
        return False


def empty_space(position) -> bool:
    """An if-statement to validate whether
    the chosen space is free or not"""
    if game_board[position] == " ":
        return True
    else:
        return False


def print_instructions_() -> None:
    """Function to print the instructions to the terminal"""
    print("Welcome to the minimax noughts and crosses game.")
    print("Input the number to place your marker in that location.\n")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9\n")
    print(f"A.I moves first. A.I plays {ai}. Human plays {player}. Good luck!")
    time.sleep(2)


def print_game_board(board: dict) -> None:
    """Function to print the current game to terminal
    using the current game board dictionary as input"""
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]}\n")


def get_player_input(player_icon):
    while True:
        # Input must be a number from 1-9 inclusive:
        try:
            while True:
                position = int(input(f"Make your move {player_icon}: "))
                # Checks position availability
                if empty_space(position):
                    break
                else:
                    print("That position is already occupied, try again.")
        except ValueError:
            print("Invalid input try again!")
            continue
        else:
            insert_icon(player_icon, position)
            print_game_board(game_board)
            break


def check_for_draw() -> bool:
    """Checks the board for a draw by
    finding any empty strings in the values
    of the keys."""
    for key in game_board.keys():
        if game_board[key] == " ":
            return False
    return True


def insert_icon(icon, position):
    """Inserts the icon into the game board
    dictionary and then checks for a draw or win.
    Exits the game if any of these cases are True"""
    if empty_space(position):
        game_board[position] = icon
        print_game_board(game_board)
        if check_for_draw():
            print("The game is a draw")
            exit()
        if check_for_winner():
            if icon == "X":
                print("Player wins!")
                print("Thanks for playing the minimax noughts and crosses A.I!")
                exit()
            else:
                print("A.I wins!")
                print("Thanks for playing the minimax noughts and crosses A.I!")
                exit()
        return


def ai_input() -> None:
    """Gets the AI's move decision"""
    high_score = -800
    best_choice = 0

    for key in game_board.keys():
        if game_board[key] == " ":
            game_board[key] = ai
            score = minimax_decision(game_board, 0, False)
            game_board[key] = " "
            if score > high_score:
                high_score = score
                best_choice = key
    insert_icon(ai, best_choice)
    return


def minimax_decision(current_game_board, depth, maximiser):
    """Minimax"""
    if check_who_won(ai):
        return 1
    elif check_who_won(player):
        return -1
    elif check_for_draw():
        return 0

    if maximiser:
        high_score = -800
        for key in current_game_board.keys():
            if current_game_board[key] == " ":
                current_game_board[key] = ai
                score = minimax_decision(current_game_board, depth + 1, False)
                current_game_board[key] = " "
                if score > high_score:
                    high_score = score
        return high_score

    else:
        high_score = 800
        for key in game_board.keys():
            if game_board[key] == " ":
                game_board[key] = player
                score = minimax_decision(game_board, depth + 1, True)
                game_board[key] = " "
                if score < high_score:
                    high_score = score
        return high_score


if __name__ == "__main__":
    print_instructions_()
    while not check_for_winner():
        ai_input()
        get_player_input(player)
