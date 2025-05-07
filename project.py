import random

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the current game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if the current player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, PLAYER_X):
        return -10 + depth
    if check_win(board, PLAYER_O):
        return 10 - depth
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI (Player O)
def find_best_move(board):
    best_move = None
    best_value = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_value = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player X's turn (human player)
        print("\nPlayer X's turn:")
        x, y = map(int, input("Enter row and column (0-2): ").split())
        if board[x][y] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[x][y] = PLAYER_X
        print_board(board)

        if check_win(board, PLAYER_X):
            print("Player X wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI's turn (Player O)
        print("\nAI's turn:")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = PLAYER_O
        print_board(board)

        if check_win(board, PLAYER_O):
            print("Player O (AI) wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()


import random

# Constants for the game
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the current game board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if the current player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in range(3):
        if all([cell == player for cell in board[row]]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, PLAYER_X):
        return -10 + depth
    if check_win(board, PLAYER_O):
        return 10 - depth
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI (Player O)
def find_best_move(board):
    best_move = None
    best_value = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_value = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player X's turn (human player)
        print("\nPlayer X's turn:")
        x, y = map(int, input("Enter row and column (0-2): ").split())
        if board[x][y] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[x][y] = PLAYER_X
        print_board(board)

        if check_win(board, PLAYER_X):
            print("Player X wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # AI's turn (Player O)
        print("\nAI's turn:")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = PLAYER_O
        print_board(board)

        if check_win(board, PLAYER_O):
            print("Player O (AI) wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
