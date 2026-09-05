"""
Tic-Tac-Toe: Human (X) vs Computer (O)
The computer uses the Minimax algorithm, so it plays perfectly —
it will never lose. Best you can do is force a draw.
"""

import math

board = [" " for _ in range(9)]

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def print_board():
    print()
    for r in range(3):
        row = board[r * 3: r * 3 + 3]
        print(" " + " | ".join(row))
        if r < 2:
            print("---+---+---")
    print()


def check_winner(b):
    for a, c, d in WIN_LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    if " " not in b:
        return "draw"
    return None


def minimax(b, is_maximizing):
    result = check_winner(b)
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "draw":
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best


def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def get_human_move():
    while True:
        raw = input("Your move (1-9, left to right, top to bottom): ").strip()
        if not raw.isdigit() or not (1 <= int(raw) <= 9):
            print("Enter a number from 1 to 9.")
            continue
        idx = int(raw) - 1
        if board[idx] != " ":
            print("That cell is already taken. Try again.")
            continue
        return idx


def main():
    print("Tic-Tac-Toe — you are X, computer is O.")
    print("Cell positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    print_board()

    while True:
        # Human turn
        idx = get_human_move()
        board[idx] = "X"
        print_board()

        result = check_winner(board)
        if result:
            announce(result)
            break

        # Computer turn
        print("Computer is thinking...")
        idx = best_move()
        board[idx] = "O"
        print_board()

        result = check_winner(board)
        if result:
            announce(result)
            break


def announce(result):
    if result == "draw":
        print("It's a draw!")
    elif result == "X":
        print("You win! (That shouldn't happen if the AI played correctly.)")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    while True:
        main()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        board = [" " for _ in range(9)]