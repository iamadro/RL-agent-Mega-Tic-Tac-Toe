import tkinter as tk
from tkinter import messagebox

class MegaTicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Mega Tic-Tac-Toe")
        self.boxes = []
        self.buttons = []
        self.mini_winners = [""] * 9
        self.mini_boards = [[""]*9 for _ in range(9)]
        self.current_player = "X"
        self.shouldReset = False

        self.win_states = ((0,1,2), (3,4,5), (6,7,8),
                           (0,3,6), (1,4,7), (2,5,8),
                           (0,4,8), (2,4,6))

    def create_mega_board(self):
        for r in range(3):
            row = []
            for c in range(3):
                box = tk.Frame(self.window, height = 200, width = 200, bd = 2, relief = 'solid')
                box.grid(row = r, column = c)
                row.append(box)
            self.boxes.append(row)
        self.create_mini_boards()

    def create_mini_boards(self):
        for r in range(9):
            row = []
            for c in range(9):
                button = tk.Button(self.boxes[r//3][c//3], text = "", font = ("Arial", 12, "bold"), height=2, width=5, background='yellow',
                                command=lambda r = r, c = c: self.make_move(r, c))
                button.grid(row=r, column=c)
                row.append(button)
            self.buttons.append(row)
    
    def make_move(self, r, c):
        # print("box: ", self.mini_boards)
        if self.buttons[r][c]["text"] == "" and self.buttons[r][c]["background"] == "yellow":
            self.buttons[r][c]["text"] = self.current_player
            box_ind = 3 * (r//3) + (c//3)
            cell_ind = 3 * (r % 3) + (c % 3)
            self.mini_boards[box_ind][cell_ind] = self.current_player

            # Checking for winner
            if self.buttons[r][c]["background"] == "yellow":
                self.check_mini_winner(box_ind)
            # print(f"Board at that box: {self.mini_boards[box_ind]}")
            if self.shouldReset:
                self.shouldReset = False
                return

            self.current_player = "O" if self.current_player == "X" else "X"
        
            for i in range(9):
                if self.mini_winners[i] != "": continue
                # print("Changing BG Iterating: ", i)
                if self.mini_winners[cell_ind] == "":
                    if i == cell_ind:
                        self.change_box_bg(i, "yellow")
                    else:
                        self.change_box_bg(i, "white")
                else:
                    self.change_box_bg(i, "yellow")


    def check_mini_winner(self, box_ind):
        for (i,j,k) in self.win_states:
            if self.mini_boards[box_ind][i] != "" and self.mini_boards[box_ind][i] == self.mini_boards[box_ind][j] == self.mini_boards[box_ind][k]:
                # print("Winner: ", self.current_player)
                self.mini_winners[box_ind] = self.current_player
                self.change_box_bg(box_ind, 'green' if self.current_player == "X" else 'red')
                self.check_final_winner()
                break

    def change_box_bg(self, box_ind, bgcolor):
        box_row = (box_ind // 3) * 3
        box_col = (box_ind % 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                self.buttons[r][c]["background"] = bgcolor

    def check_final_winner(self):
        for (i,j,k) in self.win_states:
            if self.mini_winners[i] != "" and self.mini_winners[i] == self.mini_winners[j] == self.mini_winners[k]:
                messagebox.showinfo("Game Over", f"{self.current_player} won this round!!!")
                # print("Ultimate Winner: ", self.current_player)
                self.reset()
    
    def reset(self):
        self.shouldReset = True
        for r in range(9):
            for c in range(9):
                self.buttons[r][c]["text"] = ""
                self.buttons[r][c]["background"] = "yellow"
        self.mini_winners = [""] * 9
        self.mini_boards = [[""]*9 for _ in range(9)]
        self.current_player = "X"

    def run(self):
        self.create_mega_board()
        self.window.mainloop()

game = MegaTicTacToe()
game.run()