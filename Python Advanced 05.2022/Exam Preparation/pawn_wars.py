def attempt_capture_black():

    condition = False

    if row_w - 1 in range(0, len(matrix)) and col_w - 1 in range(0, len(matrix)) and \
            row_w - 1 in range(0, len(matrix)) and col_w + 1 in range(0, len(matrix)):
        if matrix[row_w - 1][col_w - 1] == "b":
            print(f"Game over! White win, capture on {pos_col_dict[col_b]}{pos_row_dict[row_b]}.")
            condition = True

        elif matrix[row_w - 1][col_w + 1] == "b":
            print(f"Game over! White win, capture on {pos_col_dict[col_b]}{pos_row_dict[row_b]}.")
            condition = True

    elif row_w - 1 in range(0, len(matrix)) and col_w - 1 in range(0, len(matrix)):
        if matrix[row_w - 1][col_w - 1] == "b":
            print(f"Game over! White win, capture on {pos_col_dict[col_b]}{pos_row_dict[row_b]}.")
            condition = True

    elif row_w - 1 in range(0, len(matrix)) and col_w + 1 in range(0, len(matrix)):
        if matrix[row_w - 1][col_w + 1] == "b":
            print(f"Game over! White win, capture on {pos_col_dict[col_b]}{pos_row_dict[row_b]}.")
            condition = True

    return condition


def attempt_capture_white():

    condition = False

    if row_b + 1 in range(0, len(matrix)) and col_b - 1 in range(0, len(matrix)) and \
            row_b + 1 in range(0, len(matrix)) and col_b + 1 in range(0, len(matrix)):

        if matrix[row_b + 1][col_b - 1] == "w":
            print(f"Game over! Black win, capture on {pos_col_dict[col_w]}{pos_row_dict[row_w]}.")
            condition = True

        elif matrix[row_b + 1][col_b + 1] == "w":
            print(f"Game over! Black win, capture on {pos_col_dict[col_w]}{pos_row_dict[row_w]}.")
            condition = True

    elif row_b + 1 in range(0, len(matrix)) and col_b - 1 in range(0, len(matrix)):
        if matrix[row_b + 1][col_b - 1] == "w":
            print(f"Game over! Black win, capture on {pos_col_dict[col_w]}{pos_row_dict[row_w]}.")
            condition = True

    elif row_b + 1 in range(0, len(matrix)) and col_b + 1 in range(0, len(matrix)):
        if matrix[row_b + 1][col_b + 1] == "w":
            print(f"Game over! Black win, capture on {pos_col_dict[col_w]}{pos_row_dict[row_w]}.")
            condition = True

    return condition


matrix = []

pos_col_dict = {0: "a",
                1: "b",
                2: "c",
                3: "d",
                4: "e",
                5: "f",
                6: "g",
                7: "h"}

pos_row_dict = {0: "8",
                1: "7",
                2: "6",
                3: "5",
                4: "4",
                5: "3",
                6: "2",
                7: "1"}

white_pawn_pos = None
black_pawn_pos = None

for row in range(0, 8):
    current_list = [el for el in input().split()]
    matrix.append(current_list)

for row in range(0, 8):
    for col in range(0, 8):
        if matrix[row][col] == "w":
            white_pawn_pos = (row, col)

for row in range(0, 8):
    for col in range(0, 8):
        if matrix[row][col] == "b":
            black_pawn_pos = (row, col)

row_w = white_pawn_pos[0]
col_w = white_pawn_pos[1]

row_b = black_pawn_pos[0]
col_b = black_pawn_pos[1]

pawn_captured = False

while True:

    # check for capture before first move white
    black_pawn_captured = attempt_capture_black()

    if black_pawn_captured:
        break

    matrix[row_w][col_w] = "-"
    matrix[row_w - 1][col_w] = "w"
    row_w -= 1

    # check for capture before first move black
    white_pawn_captured = attempt_capture_white()

    if white_pawn_captured:
        break

    matrix[row_b][col_b] = "-"
    matrix[row_b + 1][col_b] = "b"
    row_b += 1

    if row_w == 0:
        print(f"Game over! White pawn is promoted to a queen at {pos_col_dict[col_w]}8.")
        break

    if row_b == 7:
        print(f"Game over! Black pawn is promoted to a queen at {pos_col_dict[col_b]}1.")
        break
