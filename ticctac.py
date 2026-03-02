import math

# Game board
board = [" " for _ in range(9)]

HUMAN = "X"
AI = "O"


# ---------------- DISPLAY BOARD ----------------
def print_board():
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")


# ---------------- WIN CHECK ----------------
def check_winner(player):
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False


def is_draw():
    return " " not in board


# ---------------- MINIMAX ALGORITHM ----------------
def minimax(is_maximizing):

    if check_winner(AI):
        return 1
    if check_winner(HUMAN):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = AI
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# ---------------- AI MOVE ----------------
def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = AI


# ---------------- HUMAN MOVE ----------------
def human_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
            else:
                board[move] = HUMAN
                break
        except:
            print("Enter a number between 1 and 9.")


# ---------------- GAME LOOP ----------------
def play_game():

    print("🤖 TIC-TAC-TOE AI (MINIMAX)")
    print("\nBoard positions:")

    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    print_board()

    while True:

        # Human turn
        human_move()
        print_board()

        if check_winner(HUMAN):
            print("🎉 You Win!")
            break

        if is_draw():
            print("It's a Draw!")
            break

        # AI turn
        print("AI is thinking...")
        ai_move()
        print_board()

        if check_winner(AI):
            print("🤖 AI Wins!")
            break

        if is_draw():
            print("It's a Draw!")
            break


# Start game
play_game()