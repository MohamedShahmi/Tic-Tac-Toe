import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("450x500")
window.configure(bg="#FFDAB9")  
window.minsize(450, 500)  

# Current player
current_player = "X"
x_count = 0
o_count = 0
selected_piece = None

buttons = [[None for _ in range(3)] for _ in range(3)]

BUTTON_BG = "#FFFAF0"
WINNER_BG = "lightgreen"
SELECTED_BG = "yellow"
ACTIVE_BG = "#E6E6FA"

def highlight_winner(winning_positions):
    for (r, c) in winning_positions:
        buttons[r][c].config(bg=WINNER_BG)

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            highlight_winner([(row, 0), (row, 1), (row, 2)])
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            highlight_winner([(0, col), (1, col), (2, col)])
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return True
    return False

def check_tie():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True

# Ask to play again
def ask_play_again(message):
    answer = messagebox.askyesno("Game Over", f"{message}\n\nDo you want to play again?")
    if answer:
        reset_board()
    else:
        window.destroy()

def on_click(row, col):
    global current_player, x_count, o_count, selected_piece

    if buttons[row][col]["text"] == "" and (x_count < 3 and current_player == "X" or o_count < 3 and current_player == "O"):
        buttons[row][col]["text"] = current_player
        if current_player == "X":
            buttons[row][col].config(fg="#FF4500")  
            x_count += 1
        else:
            buttons[row][col].config(fg="#1E90FF") 
            o_count += 1

        if check_winner():
            window.after(300, lambda: ask_play_again(f"Player {current_player} wins!")) 
        elif check_tie():
            window.after(300, lambda: ask_play_again("It's a Tie!"))
        else:
            current_player = "O" if current_player == "X" else "X"
    
    elif (x_count >= 3 and current_player == "X") or (o_count >= 3 and current_player == "O"):
        if selected_piece is None and buttons[row][col]["text"] == current_player:
            selected_piece = (row, col)
            buttons[row][col].config(bg=SELECTED_BG)
        elif selected_piece is not None and buttons[row][col]["text"] == "":
            buttons[row][col]["text"] = current_player
            buttons[row][col].config(fg="#FF4500" if current_player == "X" else "#1E90FF")
            old_row, old_col = selected_piece
            buttons[old_row][old_col]["text"] = ""
            buttons[old_row][old_col].config(bg=BUTTON_BG)
            selected_piece = None
            if check_winner():
                window.after(300, lambda: ask_play_again(f"Player {current_player} wins!"))
            elif check_tie():
                window.after(300, lambda: ask_play_again("It's a Tie!"))
            else:
                current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player, x_count, o_count, selected_piece
    current_player = "X"
    x_count = 0
    o_count = 0
    selected_piece = None
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].config(fg="black", bg=BUTTON_BG)

# Center frame
frame = tk.Frame(window, bg="#FFFACD")
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Grid configuration
for row in range(3):
    frame.rowconfigure(row, weight=1)
    frame.columnconfigure(row, weight=1)
    for col in range(3):
        buttons[row][col] = tk.Button(
            frame, 
            text="", 
            font=("Comic Sans MS", 30, "bold"), 
            bg=BUTTON_BG, 
            activebackground=ACTIVE_BG,
            bd=5, 
            relief="ridge",
            command=lambda r=row, c=col: on_click(r, c)
        )
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Start the GUI loop
window.mainloop()
