import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True

# Function to check if there's a winner
def check_winner(board):
    # Rowsr
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]

    return None

# Function to get available moves
def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                moves.append((i, j))
    return moves

# Minimax algorithm for AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)

    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ''
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ''
            best_score = min(score, best_score)
        return best_score

# Function for AI move (Minimax algorithm)
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move[0]][move[1]] = 'O'
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = ''
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move[0]][best_move[1]] = 'O'

# Function for user move
def player_move(board):
    while True:
        row = int(input("Enter row (1, 2, 3): ")) - 1
        col = int(input("Enter column (1, 2, 3): ")) - 1
        if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == '':
            board[row][col] = 'X'
            break
        else:
            print("Invalid move. Try again.")

# Main game function
def tic_tac_toe():
    board = [['' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'.")
    print_board(board)

    while True:
        # Player's move
        print("Your move:")
        player_move(board)
        print_board(board)

        if check_winner(board) == 'X':
            print("Congratulations, you win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_move(board)
        print_board(board)

        if check_winner(board) == 'O':
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

# Run the game
tic_tac_toe()
