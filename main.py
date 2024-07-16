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











# My code 👇

# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
#
# board = [row1, row2, row3]
# # print(f"{row1}\n{row2}\n{row3}")
#
#
# user1 = input("Who is player1?: ").upper()
# user1_symbol = input("What symbol do you choose?: X or O?: ").upper()
# user2 = input("Who is player2?: ").upper()
# user2_symbol = "O" if user1_symbol == "X" else "X"
# print(f"{user2} will have {user2_symbol}")
#
# # Game loop
# current_player = user1
# current_symbol = user1_symbol
#
# def print_board():
#     for row in board:
#         print(" ".join(row))
#
# # print_board()
#
#
# def check_win(symbol):
#
#     # check row
#     for row in board:
#         if all(cell == symbol for cell in row):
#             return True
#
#     # check column
#     for col in range(3):
#         if all(board[row][col] == symbol for row in range(3)):
#             return True
#
#     # check diagonal
#     if all(board[i][i] == symbol for i in range(3)):
#         return True
#     if all(board[i][2-i] == symbol for i in range(3)):
#         return True
#
# def check_draw():
#     for row in board:
#         for cell in row:
#             if cell == "⬜️":
#                 return False
#     return True
#
#
# while True:
#     print_board()
#     position = input(f"{current_player} enter your move (row and column, e.g., 23 for row 2, column 3): ")
#     row = int(position[0]) - 1
#     col = int(position[1]) - 1
#
#     if board[row][col] != "⬜️":
#         print("Invalid move, Try again!")
#         continue
#
#     board[row][col] = current_symbol
#
#     if check_win(current_symbol):
#         print_board()
#         print(f"Congratulations {current_player}")
#         break
#
#     if check_draw():
#         print_board()
#         print("It's a draw")
#         break
#
#     if current_player == user1:
#         current_player = user2
#         current_symbol = user2_symbol
#     else:
#         current_player = user1
#         current_symbol = user1_symbol
















#
# # Initialize the board
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
#
# board = [row1, row2, row3]
#
# def print_board():
#     for row in board:
#         print(" ".join(row))
#
# def check_win(symbol):
#     # Check rows
#     for row in board:
#         if all(s == symbol for s in row):
#             return True
#     # Check columns
#     for col in range(3):
#         if all(board[row][col] == symbol for row in range(3)):
#             return True
#     # Check diagonals
#     if all(board[i][i] == symbol for i in range(3)):
#         return True
#     if all(board[i][2 - i] == symbol for i in range(3)):
#         return True
#     return False
#
# # def check_draw():
# #     return all(all(cell != "⬜️" for cell in row) for row in board)
#
# # Alternate explanation for above.👆
# def check_draw():
#     for row in board:
#         for cell in row:
#             if cell == "⬜️":
#                 return False
#     return True
#
# # Get player names and symbols
# user1 = input("Who is player1?: ")
# user1_symbol = input("What symbol do you choose?: X or O?: ")
#
# user2 = input("Who is player2?: ")
# user2_symbol = "O" if user1_symbol == "X" else "X"
#
# print(f"{user2} will have {user2_symbol}")
#
# # Game loop
# current_player = user1
# current_symbol = user1_symbol
#
# while True:
#     print_board()
#     position = input(f"{current_player}, enter your move (row and column, e.g., 23 for row 2, column 3): ")
#     row = int(position[0]) - 1
#     col = int(position[1]) - 1
#
#     if board[row][col] != "⬜️":
#         print("Invalid move! Try again.")
#         continue
#
#     board[row][col] = current_symbol
#
#     if check_win(current_symbol):
#         print_board()
#         print(f"Congratulations {current_player}, you win!")
#         break
#
#     if check_draw():
#         print_board()
#         print("It's a draw!")
#         break
#
#     # Switch players
#     if current_player == user1:
#         current_player = user2
#         current_symbol = user2_symbol
#     else:
#         current_player = user1
#         current_symbol = user1_symbol
