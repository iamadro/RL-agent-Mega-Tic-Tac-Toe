import tkinter as tk
from tkinter import messagebox
import math
import random as rand

class MinimaxAgent:
    def __init__(self, player="O"):
        self.player = player
        self.opponent = "X"

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner == "O":
            return 10 - depth
        elif winner == "X":
            return depth - 10
        elif " " not in board:
            return 0
        
        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = " "
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == " ":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = " "
                    best_score = min(best_score, score)
            return best_score

    def find_best_move(self, board):
        best_score = -math.inf
        best_move = -1
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = self.minimax(board, 0, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def check_winner(self, board):
        win_states = [(0,1,2), (3,4,5), (6,7,8), 
                      (0,3,6), (1,4,7), (2,5,8), 
                      (0,4,8), (2,4,6)]
        for i, j, k in win_states:
            if board[i] == board[j] == board[k] and board[i] != " ":
                return board[i]
        return None

class TicTacToe:
    def __init__(self, *, difficulty):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" "] * 9  # 3x3 board as a list
        self.buttons = []
        self.agent = MinimaxAgent("O")

        self.difficulty = difficulty

        self.create_board()

    def create_board(self):
        """Creates the Tic-Tac-Toe board using buttons."""
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text=" ", font=("Arial", 24), width=5, height=2, 
                                   command=lambda x=i, y=j: self.make_move(x, y))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        """Handles a move when a button is clicked."""
        index = row * 3 + col
        if self.board[index] == " " and self.current_player == "X":
            self.board[index] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()
                return
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_game()
                return
            
            self.current_player = "O"
            self.E_greedy()

    def E_greedy(self):
        if self.difficulty > rand.random():
            self.ai_move()
        else:
            self.agent_random()
    
    def agent_random(self):
        valid_choices = [i for i in range(9) if self.board[i] == " "]
        choice = rand.choice(valid_choices)
        self.board[choice] = "O"
        row, col = divmod(choice, 3)
        self.buttons[row][col]["text"] = "O"

        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            self.reset_game()
            return
        elif " " not in self.board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.reset_game()
            return
        
        self.current_player = "X"        

    def ai_move(self):
        """Makes a move for the AI player using Minimax."""
        best_move = self.agent.find_best_move(self.board)
        if best_move != -1:
            self.board[best_move] = "O"
            row, col = divmod(best_move, 3)
            self.buttons[row][col]["text"] = "O"

        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            self.reset_game()
            return
        elif " " not in self.board:
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.reset_game()
            return
        
        self.current_player = "X"

    def check_winner(self):
        """Checks if there is a winner."""
        win_states = [(0,1,2), (3,4,5), (6,7,8), 
                      (0,3,6), (1,4,7), (2,5,8), 
                      (0,4,8), (2,4,6)]
        for i, j, k in win_states:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != " ":
                return self.board[i]  # "X" or "O"
        return None

    def reset_game(self):
        """Resets the game board."""
        self.board = [" "] * 9
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button["text"] = " "

    def run(self):
        """Runs the Tkinter main loop."""
        self.window.mainloop()

# Run the game
game = TicTacToe(difficulty = 0.5) 
game.run()
