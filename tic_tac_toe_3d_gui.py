# import tkinter as tk
# from tkinter import messagebox, simpledialog
# import random

# # === Logic Setup ===
# def create_board():
#     return [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]

# def is_valid_move(board, z, y, x):
#     return board[z][y][x] == ' '

# def get_empty_cells(board):
#     return [(z, y, x) for z in range(4) for y in range(4) for x in range(4) if board[z][y][x] == ' ']

# def generate_winning_lines():
#     lines = []
#     for z in range(4):
#         for y in range(4):
#             lines.append([(z, y, x) for x in range(4)])
#         for x in range(4):
#             lines.append([(z, y, x) for y in range(4)])
#     for y in range(4):
#         for x in range(4):
#             lines.append([(z, y, x) for z in range(4)])
#     for z in range(4):
#         lines.append([(z, i, i) for i in range(4)])
#         lines.append([(z, i, 3 - i) for i in range(4)])
#     for y in range(4):
#         lines.append([(i, y, i) for i in range(4)])
#         lines.append([(i, y, 3 - i) for i in range(4)])
#     for x in range(4):
#         lines.append([(i, i, x) for i in range(4)])
#         lines.append([(i, 3 - i, x) for i in range(4)])
#     lines.append([(i, i, i) for i in range(4)])
#     lines.append([(i, i, 3 - i) for i in range(4)])
#     lines.append([(i, 3 - i, i) for i in range(4)])
#     lines.append([(3 - i, i, i) for i in range(4)])
#     return lines

# def check_winner(board, symbol):
#     for line in WINNING_LINES:
#         if all(board[z][y][x] == symbol for z, y, x in line):
#             return line
#     return None

# def is_board_full(board):
#     return all(board[z][y][x] != ' ' for z in range(4) for y in range(4) for x in range(4))

# def evaluate(board):
#     if check_winner(board, 'O'):
#         return 100
#     elif check_winner(board, 'X'):
#         return -100
#     else:
#         return 0

# def minimax(board, depth, alpha, beta, maximizing_player):
#     score = evaluate(board)
#     if abs(score) == 100 or depth == 0 or is_board_full(board):
#         return score
#     if maximizing_player:
#         max_eval = -float('inf')
#         for z, y, x in get_empty_cells(board):
#             board[z][y][x] = 'O'
#             eval_score = minimax(board, depth - 1, alpha, beta, False)
#             board[z][y][x] = ' '
#             max_eval = max(max_eval, eval_score)
#             alpha = max(alpha, eval_score)
#             if beta <= alpha:
#                 break
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for z, y, x in get_empty_cells(board):
#             board[z][y][x] = 'X'
#             eval_score = minimax(board, depth - 1, alpha, beta, True)
#             board[z][y][x] = ' '
#             min_eval = min(min_eval, eval_score)
#             beta = min(beta, eval_score)
#             if beta <= alpha:
#                 break
#         return min_eval

# def ai_move_smart():
#     best_score = -float('inf')
#     best_move = None
#     for z, y, x in get_empty_cells(board):
#         board[z][y][x] = 'O'
#         score = minimax(board, difficulty - 1, -float('inf'), float('inf'), False)
#         board[z][y][x] = ' '
#         if score > best_score:
#             best_score = score
#             best_move = (z, y, x)
#     if best_move:
#         z, y, x = best_move
#         board[z][y][x] = 'O'
#         return z, y, x
#     return None

# # === GUI Setup ===
# root = tk.Tk()
# root.title("3D Tic Tac Toe")

# buttons = [[None for _ in range(4)] for _ in range(4)]
# layer_label = tk.Label(root, text="Layer 1", font=("Arial", 14))
# layer_label.grid(row=0, column=0, columnspan=4)

# current_layer = 0
# difficulty = 2
# board = create_board()
# WINNING_LINES = generate_winning_lines()

# def update_gui():
#     layer_label.config(text=f"Layer {current_layer+1}")
#     for y in range(4):
#         for x in range(4):
#             symbol = board[current_layer][y][x]
#             buttons[y][x].config(text=symbol, bg='SystemButtonFace')
#             if symbol != ' ':
#                 buttons[y][x].config(state='disabled')
#             else:
#                 buttons[y][x].config(state='normal')

# def restart_game():
#     global board, current_layer
#     board = create_board()
#     current_layer = 0
#     update_gui()

# def highlight_winner(line, color):
#     for z, y, x in line:
#         if z == current_layer:
#             buttons[y][x].config(bg=color)

# def handle_click(y, x):
#     global current_layer
#     if board[current_layer][y][x] == ' ':
#         board[current_layer][y][x] = 'X'
#         update_gui()
#         line = check_winner(board, 'X')
#         if line:
#             highlight_winner(line, 'green')
#             messagebox.showinfo("Game Over", "🎉 You Win!")
#             return
#         if is_board_full(board):
#             messagebox.showinfo("Game Over", "It's a draw!")
#             return
#         move = ai_move_smart()
#         update_gui()
#         if move:
#             line = check_winner(board, 'O')
#             if line:
#                 highlight_winner(line, 'red')
#                 messagebox.showinfo("Game Over", "💻 AI Wins!")
#                 return
#         if is_board_full(board):
#             messagebox.showinfo("Game Over", "It's a draw!")

# for y in range(4):
#     for x in range(4):
#         btn = tk.Button(root, text=' ', width=6, height=3, font=("Arial", 16),
#                         command=lambda y=y, x=x: handle_click(y, x))
#         btn.grid(row=y+1, column=x)
#         buttons[y][x] = btn

# def next_layer():
#     global current_layer
#     current_layer = (current_layer + 1) % 4
#     update_gui()

# def prev_layer():
#     global current_layer
#     current_layer = (current_layer - 1) % 4
#     update_gui()

# tk.Button(root, text="⏪ Prev Layer", command=prev_layer).grid(row=6, column=0, columnspan=2)
# tk.Button(root, text="Next Layer ⏩", command=next_layer).grid(row=6, column=2, columnspan=2)
# tk.Button(root, text="🔄 Restart", command=restart_game, fg="blue").grid(row=7, column=0, columnspan=4, pady=10)

# def ask_difficulty():
#     global difficulty
#     response = simpledialog.askstring("Difficulty", "Choose difficulty (easy, difficult, insane):", parent=root)
#     difficulty = {'easy': 2, 'difficult': 4, 'insane': 6}.get(response.lower(), 2) if response else 2

# ask_difficulty()
# update_gui()
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import random

# # === Logic Setup ===
# def create_board():
#     return [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]

# def is_valid_move(board, z, y, x):
#     return board[z][y][x] == ' '

# def get_empty_cells(board):
#     return [(z, y, x) for z in range(4) for y in range(4) for x in range(4) if board[z][y][x] == ' ']

# def generate_winning_lines():
#     lines = []
#     for z in range(4):
#         for y in range(4):
#             lines.append([(z, y, x) for x in range(4)])
#         for x in range(4):
#             lines.append([(z, y, x) for y in range(4)])
#     for y in range(4):
#         for x in range(4):
#             lines.append([(z, y, x) for z in range(4)])
#     for z in range(4):
#         lines.append([(z, i, i) for i in range(4)])
#         lines.append([(z, i, 3 - i) for i in range(4)])
#     for y in range(4):
#         lines.append([(i, y, i) for i in range(4)])
#         lines.append([(i, y, 3 - i) for i in range(4)])
#     for x in range(4):
#         lines.append([(i, i, x) for i in range(4)])
#         lines.append([(i, 3 - i, x) for i in range(4)])
#     lines.append([(i, i, i) for i in range(4)])
#     lines.append([(i, i, 3 - i) for i in range(4)])
#     lines.append([(i, 3 - i, i) for i in range(4)])
#     lines.append([(3 - i, i, i) for i in range(4)])
#     return lines

# def check_winner(board, symbol):
#     for line in WINNING_LINES:
#         if all(board[z][y][x] == symbol for z, y, x in line):
#             return line
#     return None

# def is_board_full(board):
#     return all(board[z][y][x] != ' ' for z in range(4) for y in range(4) for x in range(4))

# def evaluate(board):
#     if check_winner(board, 'O'):
#         return 100
#     elif check_winner(board, 'X'):
#         return -100
#     else:
#         return 0

# def minimax(board, depth, alpha, beta, maximizing_player):
#     score = evaluate(board)
#     if abs(score) == 100 or depth == 0 or is_board_full(board):
#         return score
#     if maximizing_player:
#         max_eval = -float('inf')
#         for z, y, x in get_empty_cells(board):
#             board[z][y][x] = 'O'
#             eval_score = minimax(board, depth - 1, alpha, beta, False)
#             board[z][y][x] = ' '
#             max_eval = max(max_eval, eval_score)
#             alpha = max(alpha, eval_score)
#             if beta <= alpha:
#                 break
#         return max_eval
#     else:
#         min_eval = float('inf')
#         for z, y, x in get_empty_cells(board):
#             board[z][y][x] = 'X'
#             eval_score = minimax(board, depth - 1, alpha, beta, True)
#             board[z][y][x] = ' '
#             min_eval = min(min_eval, eval_score)
#             beta = min(beta, eval_score)
#             if beta <= alpha:
#                 break
#         return min_eval

# def ai_move_smart():
#     best_score = -float('inf')
#     best_move = None
#     for z, y, x in get_empty_cells(board):
#         board[z][y][x] = 'O'
#         score = minimax(board, difficulty - 1, -float('inf'), float('inf'), False)
#         board[z][y][x] = ' '
#         if score > best_score:
#             best_score = score
#             best_move = (z, y, x)
#     if best_move:
#         z, y, x = best_move
#         board[z][y][x] = 'O'
#         return z, y, x
#     return None

# # === GUI Setup ===
# def update_gui():
#     for z in range(4):
#         for y in range(4):
#             for x in range(4):
#                 symbol = board[z][y][x]
#                 btn = buttons[z][y][x]
#                 btn.config(text=symbol, bg='SystemButtonFace')
#                 btn.config(state='disabled' if symbol != ' ' else 'normal')

# def handle_click(z, y, x):
#     if board[z][y][x] == ' ':
#         board[z][y][x] = 'X'
#         update_gui()
#         line = check_winner(board, 'X')
#         if line:
#             highlight_winner(line, 'green')
#             messagebox.showinfo("Game Over", "🎉 You Win!")
#             return
#         if is_board_full(board):
#             messagebox.showinfo("Game Over", "It's a draw!")
#             return
#         move = ai_move_smart()
#         update_gui()
#         if move:
#             line = check_winner(board, 'O')
#             if line:
#                 highlight_winner(line, 'red')
#                 messagebox.showinfo("Game Over", "💻 AI Wins!")
#                 return
#         if is_board_full(board):
#             messagebox.showinfo("Game Over", "It's a draw!")

# def highlight_winner(line, color):
#     for z, y, x in line:
#         buttons[z][y][x].config(bg=color)

# def restart_game():
#     global board
#     board = create_board()
#     update_gui()

# # Initialize game
# board = create_board()
# WINNING_LINES = generate_winning_lines()
# difficulty = 2

# # Tkinter Setup
# root = tk.Tk()
# root.title("3D Tic Tac Toe - FourSight")

# main_frame = tk.Frame(root)
# main_frame.pack()

# buttons = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]

# # Create 4 side-by-side layer frames
# for z in range(4):
#     frame = tk.Frame(main_frame, padx=10, pady=10)
#     frame.grid(row=0, column=z)
#     tk.Label(frame, text=f"Layer {z+1}", font=("Arial", 14)).grid(row=0, column=0, columnspan=4)
#     for y in range(4):
#         for x in range(4):
#             btn = tk.Button(frame, text=' ', width=4, height=2, font=("Arial", 16),
#                             command=lambda z=z, y=y, x=x: handle_click(z, y, x))
#             btn.grid(row=y+1, column=x)
#             buttons[z][y][x] = btn

# tk.Button(root, text="🔄 Restart", command=restart_game, fg="blue").pack(pady=10)

# update_gui()
# root.mainloop()


import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# === Logic Setup ===
def create_board():
    return [[[' ' for _ in range(4)] for _ in range(4)] for _ in range(4)]

def is_valid_move(board, z, y, x):
    return board[z][y][x] == ' '

def get_empty_cells(board):
    return [(z, y, x) for z in range(4) for y in range(4) for x in range(4) if board[z][y][x] == ' ']

def generate_winning_lines():
    lines = []
    for z in range(4):
        for y in range(4):
            lines.append([(z, y, x) for x in range(4)])
        for x in range(4):
            lines.append([(z, y, x) for y in range(4)])
    for y in range(4):
        for x in range(4):
            lines.append([(z, y, x) for z in range(4)])
    for z in range(4):
        lines.append([(z, i, i) for i in range(4)])
        lines.append([(z, i, 3 - i) for i in range(4)])
    for y in range(4):
        lines.append([(i, y, i) for i in range(4)])
        lines.append([(i, y, 3 - i) for i in range(4)])
    for x in range(4):
        lines.append([(i, i, x) for i in range(4)])
        lines.append([(i, 3 - i, x) for i in range(4)])
    lines.append([(i, i, i) for i in range(4)])
    lines.append([(i, i, 3 - i) for i in range(4)])
    lines.append([(i, 3 - i, i) for i in range(4)])
    lines.append([(3 - i, i, i) for i in range(4)])
    return lines

def check_winner(board, symbol):
    for line in WINNING_LINES:
        if all(board[z][y][x] == symbol for z, y, x in line):
            return line
    return None

def is_board_full(board):
    return all(board[z][y][x] != ' ' for z in range(4) for y in range(4) for x in range(4))

def evaluate(board):
    if check_winner(board, 'O'):
        return 100
    elif check_winner(board, 'X'):
        return -100
    else:
        return 0

def minimax(board, depth, alpha, beta, maximizing_player):
    score = evaluate(board)
    if abs(score) == 100 or depth == 0 or is_board_full(board):
        return score
    if maximizing_player:
        max_eval = -float('inf')
        for z, y, x in get_empty_cells(board):
            board[z][y][x] = 'O'
            eval_score = minimax(board, depth - 1, alpha, beta, False)
            board[z][y][x] = ' '
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for z, y, x in get_empty_cells(board):
            board[z][y][x] = 'X'
            eval_score = minimax(board, depth - 1, alpha, beta, True)
            board[z][y][x] = ' '
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval

def ai_move_smart():
    best_score = -float('inf')
    best_move = None
    for z, y, x in get_empty_cells(board):
        board[z][y][x] = 'O'
        score = minimax(board, depth - 1, -float('inf'), float('inf'), False)
        board[z][y][x] = ' '
        if score > best_score:
            best_score = score
            best_move = (z, y, x)
    if best_move:
        z, y, x = best_move
        board[z][y][x] = 'O'
        return z, y, x
    return None

# === GUI Setup ===
def update_gui():
    for z in range(4):
        for y in range(4):
            for x in range(4):
                symbol = board[z][y][x]
                btn = buttons[z][y][x]
                btn.config(
                    text=symbol,
                    bg='black',
                    fg='white' if symbol == 'X' else ('orange' if symbol == 'O' else 'white'),
                    relief='solid',
                    borderwidth=2
                )
                btn.config(state='disabled' if symbol != ' ' else 'normal')



def handle_click(z, y, x):
    if board[z][y][x] == ' ':
        board[z][y][x] = 'X'
        update_gui()
        line = check_winner(board, 'X')
        if line:
            highlight_winner(line, 'green')
            messagebox.showinfo("Game Over", "🎉 You Win!")
            return
        if is_board_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            return
        move = ai_move_smart()
        update_gui()
        if move:
            line = check_winner(board, 'O')
            if line:
                highlight_winner(line, 'red')
                messagebox.showinfo("Game Over", "💻 AI Wins!")
                return
        if is_board_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")

def highlight_winner(line, color):
    for z, y, x in line:
        buttons[z][y][x].config(bg=color)

def restart_game():
    global board, depth
    ask_difficulty()
    board = create_board()
    update_gui()
    
def ask_difficulty():
    global depth
    response = simpledialog.askstring("Difficulty", "Choose difficulty (easy, difficult, insane):", parent=root)
    levels = {'easy': 2, 'difficult': 4, 'insane': 6}
    depth = levels.get(response.lower(), 2) if response else 2

# Initialize game
root = tk.Tk()
root.configure(bg='black')
root.title("3D Tic Tac Toe - FourSight")

ask_difficulty()

board = create_board()
WINNING_LINES = generate_winning_lines()

main_frame = tk.Frame(root)
main_frame.pack()

buttons = [[[None for _ in range(4)] for _ in range(4)] for _ in range(4)]

# Create 4 side-by-side layer frames
for z in range(4):
    frame = tk.Frame(main_frame, padx=10, pady=10, bg='black')
    frame.grid(row=0, column=z)
    tk.Label(frame, text=f"Layer {z+1}", font=("Arial", 14), bg='black', fg='lime').grid(row=0, column=0, columnspan=4)

    for y in range(4):
        for x in range(4):
            cell_frame = tk.Frame(frame, background='green', padx=1, pady=1)
            cell_frame.grid(row=y+1, column=x)
            btn = tk.Button(cell_frame, text=' ', width=4, height=2, font=("Arial", 16),bg='black', fg='white', relief='solid', bd=0,
                            command=lambda z=z, y=y, x=x: handle_click(z, y, x))
            btn.pack()
            buttons[z][y][x] = btn

tk.Button(root, text="🔄 Restart", command=restart_game, bg='black', fg='white').pack(pady=10)

update_gui()
root.mainloop()
