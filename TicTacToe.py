import tkinter
from tkinter import messagebox
import random

# Fungsi untuk menandai kotak ketika tombol diklik
def set_tile(row, column):
    global curr_player

    # Jika permainan sudah berakhir atau kotak sudah terisi, kembalikan
    if game_over or board[row][column]["text"] != "":
        return

    # Menandai kotak dengan simbol pemain saat ini (X atau O)
    board[row][column]["text"] = curr_player
    board[row][column]["fg"] = color_X if curr_player == playerX else color_O

    # Cek apakah ada pemenang setelah langkah ini
    check_winner()

    # Ganti giliran pemain
    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = curr_player + "'s turn"

    # Jika mode AI dan giliran AI, jalankan langkah AI
    if mode == "AI" and curr_player == ai_player and not game_over:
        ai_move()

# Fungsi untuk langkah AI (menggunakan random move)
def ai_move():
    # Cari semua kotak yang masih kosong
    available_moves = [(row, column) for row in range(3) for column in range(3) if board[row][column]["text"] == ""]
    if available_moves:
        # Pilih langkah secara acak dari kotak yang tersedia
        row, column = random.choice(available_moves)
        set_tile(row, column)

# Fungsi untuk mengecek apakah ada pemenang
def check_winner():
    global turns, game_over
    turns += 1  # Tambah jumlah langkah yang telah dilakukan

    # Cek baris untuk pemenang
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            winner = board[row][0]["text"]
            update_score(winner)  # Update skor
            label.config(text=winner + " pemenang!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)  # Highlight baris pemenang
            game_over = True
            set_first_player(winner)  # Set pemain pertama untuk permainan selanjutnya
            return

    # Cek kolom untuk pemenang
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            winner = board[0][column]["text"]
            update_score(winner)  # Update skor
            label.config(text=winner + " pemenang!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)  # Highlight kolom pemenang
            game_over = True
            set_first_player(winner)  # Set pemain pertama untuk permainan selanjutnya
            return

    # Cek diagonal kiri ke kanan untuk pemenang
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        winner = board[0][0]["text"]
        update_score(winner)  # Update skor
        label.config(text=winner + " pemenang!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)  # Highlight diagonal pemenang
        game_over = True
        set_first_player(winner)  # Set pemain pertama untuk permainan selanjutnya
        return

    # Cek diagonal kanan ke kiri untuk pemenang
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        winner = board[0][2]["text"]
        update_score(winner)  # Update skor
        label.config(text=winner + " pemenang!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)  # Highlight kotak pemenang
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        set_first_player(winner)  # Set pemain pertama untuk permainan selanjutnya
        return

    # Jika semua kotak terisi dan tidak ada pemenang, permainan seri
    if turns == 9:
        game_over = True
        label.config(text="Seri!", foreground=color_yellow)

# Fungsi untuk menentukan pemain pertama di permainan selanjutnya
def set_first_player(winner):
    global curr_player
    # Jika X menang, X akan bermain pertama di permainan selanjutnya
    if winner == playerX:
        curr_player = playerX
    else:
        curr_player = playerO  # Jika O menang, O akan bermain pertama

    label.config(text=curr_player + "'s turn")

# Fungsi untuk memperbarui skor
def update_score(winner):
    global scoreX, scoreO
    if winner == playerX:
        scoreX += 1  # Tambah skor X
    elif winner == playerO:
        scoreO += 1  # Tambah skor O
    score_label.config(text=f"Skor X: {scoreX} | O: {scoreO}")

# Fungsi untuk memulai permainan baru
def new_game():
    global turns, game_over
    turns = 0  # Reset jumlah langkah
    game_over = False  # Reset status permainan

    label.config(text=curr_player + "'s turn", foreground="white")
    update_mode_label()

    # Reset semua kotak ke keadaan kosong
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_X, background=color_black)

    # Jika mode AI dan AI adalah pemain pertama, jalankan langkah AI
    if mode == "AI" and curr_player == ai_player:
        ai_move()

# Fungsi untuk mengatur mode AI
def set_mode_ai():
    global mode, scoreX, scoreO, curr_player, ai_player
    mode = "AI"  # Set mode ke AI
    scoreX = 0  # Reset skor X
    scoreO = 0  # Reset skor O

    # Tampilkan dialog untuk memilih pemain (X atau O)
    choice = messagebox.askquestion("Pilih Pemain", "Apakah Anda ingin bermain sebagai X?", icon="question")
    if choice == "yes":
        curr_player = playerX  # Pemain sebagai X
        ai_player = playerO    # AI sebagai O
    else:
        curr_player = playerO  # Pemain sebagai O
        ai_player = playerX    # AI sebagai X
        # Jika pemain memilih O, AI (sebagai X) akan bergerak terlebih dahulu
        if mode == "AI" and curr_player == playerO:
            ai_move()

    label.config(text=f"Mode AI: Anda sebagai {curr_player}")
    new_game()

# Fungsi untuk mengatur mode Human (2 pemain)
def set_mode_human():
    global mode, scoreX, scoreO, curr_player
    mode = "HUMAN"  # Set mode ke Human
    scoreX = 0  # Reset skor X
    scoreO = 0  # Reset skor O
    curr_player = playerX  # Mulai dengan X ketika mode Human
    label.config(text="Mode Human: Anda sebagai " + playerX)
    new_game()

# Fungsi untuk memperbarui label mode dan skor
def update_mode_label():
    score_label.config(text=f"Skor X: {scoreX} | O: {scoreO} | Mode: {mode}")

# Set up the players and game mode
playerX = 'X'  # Simbol untuk pemain X
playerO = 'O'  # Simbol untuk pemain O
curr_player = playerX  # Pemain saat ini, dimulai dengan X
ai_player = playerO  # AI sebagai O (default)
mode = "HUMAN"  # Mode permainan, default adalah Human

scoreX = 0  # Skor untuk pemain X
scoreO = 0  # Skor untuk pemain O

# Create a 3x3 board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Papan permainan 3x3

# Warna untuk antarmuka
color_X = "#00FF00"  # Warna untuk X
color_O = "#FF00FF"  # Warna untuk O
color_yellow = "#ffde57"  # Warna untuk pesan pemenang
color_black = "#1A1A1A"  # Warna latar belakang
color_light_gray = "#646464"  # Warna untuk highlight pemenang

turns = 0  # Jumlah langkah yang telah dilakukan
game_over = False  # Status permainan

# Initialize main window
window = tkinter.Tk()
window.title("Tic Tac Toe")  # Judul window
window.resizable(False, False)  # Window tidak bisa di-resize

# Create a menu for selecting the mode
menu = tkinter.Menu(window)
mode_menu = tkinter.Menu(menu, tearoff=0)
mode_menu.add_command(label="Mode AI", command=set_mode_ai)  # Opsi untuk mode AI
mode_menu.add_command(label="Mode Human", command=set_mode_human)  # Opsi untuk mode Human
menu.add_cascade(label="Mode", menu=mode_menu)  # Tambahkan menu mode ke window
window.config(menu=menu)

# Create frame to hold the game board
frame = tkinter.Frame(window)

# Create labels for turn indication and score
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("consolas", 20), background=color_black, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")  # Label untuk giliran pemain

score_label = tkinter.Label(frame, text=f"Skor X: {scoreX} | O: {scoreO} | Mode: {mode}", font=("consolas", 15), background=color_black, foreground="white")
score_label.grid(row=1, column=0, columnspan=3, sticky="we")  # Label untuk skor dan mode

# Create buttons for the Tic Tac Toe board
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"),
                                            background=color_black, foreground=color_X, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+2, column=column)  # Tambahkan tombol ke grid

# Create restart button
button = tkinter.Button(frame, text="restart", font=("consolas", 20), background=color_black, foreground="white", command=new_game)
button.grid(row=5, column=0, columnspan=3, sticky="we")  # Tombol restart

frame.pack()

# Center the window on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")  # Posisikan window di tengah layar

window.mainloop()  # Jalankan aplikasi