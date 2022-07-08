def find_count(board_1, row_1, col_1):

    result = 0

    moves = [
        [row_1 + 2, col_1 - 1],
        [row_1 + 2, col_1 + 1],
        [row_1 + 1, col_1 - 2],
        [row_1 + 1, col_1 + 2],
        [row_1 - 1, col_1 - 2],
        [row_1 - 1, col_1 + 2],
        [row_1 - 2, col_1 - 1],
        [row_1 - 2, col_1 + 1]
    ]

    for r, c in moves:
        if 0 <= r < len(board_1) and 0 <= c < len(board_1) and board_1[r][c] == "K":
            result += 1

    return result


size_matrix = int(input())

board = []

removed_knights_counter = 0

for row in range(0, size_matrix):
    current_list = [el for el in input()]
    board.append(current_list)

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0

    for row in range(0, size_matrix):
        for col in range(0, size_matrix):

            if board[row][col] == "0":
                continue

            count = find_count(board, row, col)

            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    board[knight_row][knight_col] = "0"
    removed_knights_counter += 1

print(removed_knights_counter)
