import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = [["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"], ["⬜️", "⬜️", "⬜️"]]

# Players' details
user1 = "Player 1"
user1_symbol = "X"
user2 = "Player 2"
user2_symbol = "O"
current_player = user1
current_symbol = user1_symbol

# Function to check for a win
def check_win(symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

# Function to check for a draw
def check_draw():
    for row in board:
        for cell in row:
            if cell == "⬜️":
                return False
    return True

# Function to handle button clicks
def button_click(row, col):
    global current_player, current_symbol

    if board[row][col] != "⬜️":
        messagebox.showwarning("Invalid Move", "This cell is already taken. Try another one.")
        return

    board[row][col] = current_symbol
    buttons[row][col].config(text=current_symbol)

    if check_win(current_symbol):
        messagebox.showinfo("Congratulations", f"{current_player} wins!")
        window.quit()
    elif check_draw():
        messagebox.showinfo("Draw", "It's a draw!")
        window.quit()
    else:
        current_player = user2 if current_player == user1 else user1
        current_symbol = user2_symbol if current_symbol == user1_symbol else user1_symbol

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the buttons and grid
buttons = [[None, None, None], [None, None, None], [None, None, None]]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(window, text="⬜️", width=10, height=3, font=('Arial', 24),
                                      command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Run the main event loop
window.mainloop()
