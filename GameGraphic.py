import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Kółko i Krzyżyk")
        self.current_player = "O"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    master, text="", font=("Helvetica", 24), width=5, height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(row, col):
                messagebox.showinfo("Koniec gry", f"Gracz {self.current_player} wygrywa!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Koniec gry", "Remis!")
                self.reset_board()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self, row, col):
        # Sprawdzanie wierszy
        if all(self.board[row][i] == self.current_player for i in range(3)):
            return True
        # Sprawdzanie kolumn
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        # Sprawdzanie przekątnych
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
