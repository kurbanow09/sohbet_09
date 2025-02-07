import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("320x500")  # Daha kompakt ekran
        self.window.configure(bg="black")

        self.main_menu()

    def main_menu(self):
        """Ana menü ekranı"""
        for widget in self.window.winfo_children():
            widget.destroy()

        title = tk.Label(self.window, text="Tic Tac Toe", font=("Arial", 20, "bold"), bg="black", fg="white")
        title.pack(pady=15)

        tk.Button(self.window, text="1 Kişilik (Zor)", font=("Arial", 14), height=2, width=10,
                  command=lambda: self.start_game(single=True)).pack(pady=8)
        tk.Button(self.window, text="2 Kişilik", font=("Arial", 14), height=2, width=10,
                  command=lambda: self.start_game(single=False)).pack(pady=8)
        tk.Button(self.window, text="Çıkış", font=("Arial", 14), height=2, width=10, command=self.window.quit).pack(pady=8)

    def start_game(self, single=False):
        """Oyun tahtasını başlatır"""
        self.single_player = single
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        for widget in self.window.winfo_children():
            widget.destroy()

        self.buttons = [[tk.Button(self.window, text="", font=("Arial", 20, "bold"), width=3, height=1,
                                   command=lambda r=i, c=j: self.make_move(r, c)) 
                        for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=2, pady=2)

        self.status_label = tk.Label(self.window, text="Sıra: X", font=("Arial", 14), bg="black", fg="white")
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(self.window, text="Menüye Dön", font=("Arial", 12), command=self.main_menu).grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        """Oyuncunun hamlesini yapar"""
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")

            if self.check_winner():
                self.status_label.config(text=f"{self.current_player} Kazandı!")
                return

            if self.check_draw():
                self.status_label.config(text="Berabere!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Sıra: {self.current_player}")

            if self.single_player and self.current_player == "O":
                self.bot_move()

    def bot_move(self):
        """Güçlü bot hamlesi (MiniMax)"""
        best_move = self.minimax(self.board, True)[1]
        if best_move:
            self.make_move(best_move[0], best_move[1])

    def minimax(self, board, is_maximizing):
        """MiniMax algoritması ile en iyi hamleyi hesaplar"""
        if self.check_winner_static(board, "O"):
            return 1, None
        if self.check_winner_static(board, "X"):
            return -1, None
        if self.check_draw_static(board):
            return 0, None

        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None

        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O" if is_maximizing else "X"
                    score = self.minimax(board, not is_maximizing)[0]
                    board[r][c] = ""

                    if is_maximizing:
                        if score > best_score:
                            best_score = score
                            best_move = (r, c)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (r, c)

        return best_score, best_move

    def check_winner(self):
        """Kazananı kontrol eder"""
        return self.check_winner_static(self.board, self.current_player)

    def check_winner_static(self, board, player):
        """Belirtilen oyuncu için kazanma durumunu kontrol eder"""
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        """Beraberelik durumunu kontrol eder"""
        return self.check_draw_static(self.board)

    def check_draw_static(self, board):
        """Statik olarak berabere olup olmadığını kontrol eder"""
        return all(board[i][j] != "" for i in range(3) for j in range(3))

    def run(self):
        self.window.mainloop()

# Oyunu başlat
TicTacToe().run()