import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" "]*9  # 3x3 board as a list
        self.buttons = []

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
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[row][col]["text"] = self.current_player

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

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
        self.board = [" "]*9
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button["text"] = " "

    def run(self):
        """Runs the Tkinter main loop."""
        self.window.mainloop()

# Run the game
game = TicTacToe()
game.run()
