import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("450x500")
window.resizable(True, True)
window.configure(bg="#FFDAB9")  

# Current player
current_player = "X"
x_count = 0  # Counter for X moves
o_count = 0  # Counter for O moves
selected_piece = None  # Track which piece is selected for moving

# Create buttons
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    # Check rows, columns, and diagonals
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_tie():
    # Check if the board is full
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True

def on_click(row, col):
    global current_player, x_count, o_count, selected_piece

    # Normal moves for first 3
    if buttons[row][col]["text"] == "" and (x_count < 3 and current_player == "X" or o_count < 3 and current_player == "O"):
        buttons[row][col]["text"] = current_player
        if current_player == "X":
            buttons[row][col].config(fg="#FF4500")  
            x_count += 1
        else:
            buttons[row][col].config(fg="#1E90FF") 
            o_count += 1

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a Tie!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
    
    # If the player has made 3 moves, start the "move" action
    elif (x_count >= 3 and current_player == "X") or (o_count >= 3 and current_player == "O"):
        # If no piece is selected, select the current piece
        if selected_piece is None and buttons[row][col]["text"] == current_player:
            selected_piece = (row, col)
            buttons[row][col].config(bg="yellow")  # Highlight selected piece
        # If piece is selected, move it
        elif selected_piece is not None and buttons[row][col]["text"] == "":
            buttons[row][col]["text"] = current_player
            buttons[row][col].config(fg="#FF4500" if current_player == "X" else "#1E90FF")
            # Clear the old position of the moved piece
            old_row, old_col = selected_piece
            buttons[old_row][old_col]["text"] = ""
            buttons[old_row][old_col].config(bg="#FFFAF0")  # Reset old spot background color
            selected_piece = None  # Reset the selected piece
            current_player = "O" if current_player == "X" else "X"  # Switch player
            
            # Check for winner after moving the piece
            if check_winner():
                messagebox.showinfo("Game Over", f"Player {current_player} wins!")
                reset_board()
            elif check_tie():
                messagebox.showinfo("Game Over", "It's a Tie!")
                reset_board()

def reset_board():
    global current_player, x_count, o_count
    current_player = "X"
    x_count = 0
    o_count = 0
    selected_piece = None
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].config(fg="black", bg="#FFFAF0")  # Reset color and text

# Centered frame
frame = tk.Frame(window, bg="#FFFACD")  
frame.pack(expand=True, pady=40)

# Create colorful buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(
            frame, 
            text="", 
            font=("Comic Sans MS", 30, "bold"), 
            width=4, 
            height=2,
            bg="#FFFAF0",  
            activebackground="#E6E6FA",
            bd=5, 
            relief="ridge", 
            command=lambda r=row, c=col: on_click(r, c)
        )
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
