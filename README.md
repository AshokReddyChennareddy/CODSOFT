Tic-Tac-Toe AI: Unbeatable AI Using Minimax Algorithm
Overview:
This project implements a Tic-Tac-Toe game where the player plays against an AI. 
The AI is designed using the Minimax algorithm, making it unbeatable in this zero-sum game. 
The AI always calculates the optimal move and tries to minimize the player's chance of winning.

How It Works:
Player vs. AI: The human player plays as 'X', while the AI is assigned 'O'.
AI Strategy: The AI uses the Minimax algorithm, which considers all possible game outcomes and chooses the optimal move, ensuring that it either wins or forces a draw.
Game Flow:
The game alternates turns between the player and the AI.
The player provides their move by choosing the row and column.
The AI calculates the best move based on the current board state using Minimax.
The game ends when there's a winner or when the board is full (resulting in a tie).
Key Functions:
minimax(board, depth, is_maximizing): The core of the AI. This function recursively calculates the best possible outcome for the AI or player, ensuring optimal decisions.
ai_move(board): AI's move logic, calling Minimax to choose the best available move.
player_move(board): Accepts input from the user and updates the board.
check_winner(board): Checks if either player has won or if the game is tied.
Technology Stack:
Python: The entire game is developed using Python.
Minimax Algorithm: A basic AI algorithm used in game theory to find optimal moves in decision-making problems.
Learning Outcomes:
Understanding of game theory and search algorithms.
Hands-on experience with the Minimax algorithm.
Application of Python for game development and AI logic.
How to Run:
Simply run the script in any Python environment. The game will prompt you to enter your moves while the AI will respond with its best move.

