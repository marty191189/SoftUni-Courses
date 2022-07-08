from collections import deque


def check_invalid_pos(row_1, col_1, direction):
    if row_1 not in range(0, 6):

        if direction == "up":
            row_1 = 5

        elif direction == "down":
            row_1 = 0

    if col_1 not in range(0, 6):

        if direction == "left":
            col_1 = 5

        elif direction == "right":
            col_1 = 0

    val_pos_tuple = (row_1, col_1)

    return val_pos_tuple


matrix = []

deposits_dict = {"Water": 0, "Metal": 0, "Concrete": 0}

rover_pos = None

rover_is_broken = False

suitable_for_colony = False

for row in range(0, 6):
    current_list = [el for el in input().split()]
    matrix.append(current_list)

for row in range(0, 6):
    for col in range(0, 6):
        if matrix[row][col] == "E":
            rover_pos = (row, col)

row = rover_pos[0]
col = rover_pos[1]

commands_deque = deque([el for el in input().split(", ")])

while True:

    if not commands_deque:
        break

    if rover_is_broken:
        break

    current_command = commands_deque.popleft()

    if current_command == "up":
        row -= 1
        valid_pos_tuple = check_invalid_pos(row, col, current_command)
        row = valid_pos_tuple[0]
        col = valid_pos_tuple[1]

    elif current_command == "down":
        row += 1
        valid_pos_tuple = check_invalid_pos(row, col, current_command)
        row = valid_pos_tuple[0]
        col = valid_pos_tuple[1]

    elif current_command == "left":
        col -= 1
        valid_pos_tuple = check_invalid_pos(row, col, current_command)
        row = valid_pos_tuple[0]
        col = valid_pos_tuple[1]

    elif current_command == "right":
        col += 1
        valid_pos_tuple = check_invalid_pos(row, col, current_command)
        row = valid_pos_tuple[0]
        col = valid_pos_tuple[1]

    if matrix[row][col] == "W":
        deposits_dict["Water"] += 1
        print(f"Water deposit found at ({row}, {col})")

    elif matrix[row][col] == "M":
        deposits_dict["Metal"] += 1
        print(f"Metal deposit found at ({row}, {col})")

    elif matrix[row][col] == "C":
        deposits_dict["Concrete"] += 1
        print(f"Concrete deposit found at ({row}, {col})")

    elif matrix[row][col] == "R":
        rover_is_broken = True
        print(f"Rover got broken at ({row}, {col})")
        break

if deposits_dict["Water"] >= 1 and deposits_dict["Metal"] >= 1 and deposits_dict["Concrete"] >= 1:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
