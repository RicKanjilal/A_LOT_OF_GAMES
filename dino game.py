import tkinter as tk
import math
import copy

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 24), width=4, height=2,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 18))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled")
            if self.check_winner("X"):
                self.end_game("Player X wins!")
            elif all([cell != " " for row in self.board for cell in row]):
                self.end_game("It's a tie!")
            else:
                self.status_label.config(text="AI's turn")
                self.root.after(500, self.ai_move)

    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        row, col = best_move
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O", state="disabled")
        if self.check_winner("O"):
            self.end_game("AI wins!")
        elif all([cell != " " for row in self.board for cell in row]):
            self.end_game("It's a tie!")
        else:
            self.status_label.config(text="Player X's turn")

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("X"):
            return -10 + depth
        elif self.check_winner("O"):
            return 10 - depth
        elif all([cell != " " for row in board for cell in row]):
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2-i] == player for i in range(3)]):
            return True
        return False

    def end_game(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")
        self.status_label.config(text=message)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()