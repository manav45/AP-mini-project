import tkinter as tk

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board, row=0, col=0):
    if row == 9 - 1 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solve_sudoku(board, row, col + 1)

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, row, col + 1):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(str(elem) for elem in row))

def validate_solution(board):
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            board[i][j] = 0
            if not is_valid(board, i, j, num):
                return False
            board[i][j] = num
    return True

def on_solve():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            if entries[i][j].get():
                row.append(int(entries[i][j].get()))
            else:
                row.append(0)
        board.append(row)

    if solve_sudoku(board):
        if validate_solution(board):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, board[i][j])
            result_label.config(text="")
        else:
            result_label.config(text="The Sudoku solution is incorrect.")
    else:
        result_label.config(text="No solution found")

def reset_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

root = tk.Tk()
root.title("Sudoku Solver")

# Set window size
window_size = 500
root.geometry(f"{window_size}x{window_size}")

# Custom colors
bg_color = "#F0F0F0"  # Light Gray
entry_bg_color = "#FFFFFF"  # White
solve_btn_color = "#32CD32"  # Lime Green
reset_btn_color = "#4169E1"  # Royal Blue
result_label_color = "#FF4500"  # Orange Red

root.config(bg=bg_color)

entries = []
frames = []

# Create frames for each 3x3 subgrid
for i in range(3):
    frame_row = []
    for j in range(3):
        frame = tk.Frame(root, bg=bg_color, highlightbackground="black", highlightthickness=1)
        frame.grid(row=i, column=j, padx=1, pady=1)
        frame_row.append(frame)
    frames.append(frame_row)

# Create entry fields within each frame
for i in range(9):
    row_entries = []
    for j in range(9):
        frame = frames[i // 3][j // 3]  # Determine which frame the entry should belong to
        entry = tk.Entry(frame, width=2, font=('Helvetica', 20), bg=entry_bg_color, justify="center")
        entry.grid(row=i % 3, column=j % 3, padx=2, pady=2)
        row_entries.append(entry)
    entries.append(row_entries)

# Create Solve button
solve_button = tk.Button(root, text="Solve", command=on_solve, font=('Helvetica', 14), bg=solve_btn_color, fg="white")
solve_button.grid(row=3, column=0, columnspan=3, pady=(10, 5))

# Create Reset button
reset_button = tk.Button(root, text="Reset", command=reset_board, font=('Helvetica', 14), bg=reset_btn_color, fg="white")
reset_button.grid(row=4, column=0, columnspan=3, pady=5)

# Create Result label
result_label = tk.Label(root, text="", font=('Helvetica', 14), bg=bg_color, fg=result_label_color)
result_label.grid(row=5, column=0, columnspan=3, pady=(5, 10))

root.mainloop()
