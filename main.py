import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики с ботом")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.player = "X"  # игрок всегда X, бот — O
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 32), width=5, height=2,
                                   command=lambda r=row, c=col: self.player_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def player_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player, state="disabled")
            if self.check_winner(self.player):
                self.end_game("Вы победили!")
            elif self.is_draw():
                self.end_game("Ничья!")
            else:
                self.root.after(500, self.bot_move)  # бот думает 0.5 сек

    def bot_move(self):
        empty = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ""]
        if empty:
            row, col = random.choice(empty)
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", state="disabled")
            if self.check_winner("O"):
                self.end_game("Бот победил!")
            elif self.is_draw():
                self.end_game("Ничья!")

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or \
               all(self.board[j][i] == symbol for j in range(3)):
                return True

        if all(self.board[i][i] == symbol for i in range(3)) or \
           all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def end_game(self, message):
        messagebox.showinfo("Игра окончена", message)
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()