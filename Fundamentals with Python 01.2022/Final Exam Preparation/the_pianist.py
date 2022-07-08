number_of_pieces = int(input())

music_dict = {}

for number in range(1, number_of_pieces + 1):

    current_info = input().split("|")

    piece = current_info[0]
    composer = current_info[1]
    key_name = current_info[2]

    music_dict[piece] = []
    music_dict[piece].append(composer)
    music_dict[piece].append(key_name)

data = input()

while not data == "Stop":

    command = data.split("|")

    if command[0] == "Add":

        piece = command[1]
        composer = command[2]
        key_name = command[3]

        if piece not in music_dict:
            music_dict[piece] = []
            music_dict[piece].append(composer)
            music_dict[piece].append(key_name)
            print(f"{piece} by {composer} in {key_name} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":

        piece = command[1]

        if piece not in music_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")

        else:
            print(f"Successfully removed {piece}!")
            del music_dict[piece]

    elif command[0] == "ChangeKey":

        piece = command[1]
        new_key_name = command[2]

        if piece not in music_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")

        else:
            music_dict[piece][1] = new_key_name
            print(f"Changed the key of {piece} to {new_key_name}!")

    data = input()

for key, value in music_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")


# второ решение Инес
#
# class Piece:
#     def __init__(self, name, composer, key):
#         self.name = name
#         self.composer = composer
#         self.key = key
#
#
# pieces = []
#
# n = int(input())
#
# for _ in range(n):
#     name, composer, key = input().split("|")
#     piece = Piece(name, composer, key)
#     pieces.append(piece)
#
# data = input()
# while not data == "Stop":
#     split_data = data.split("|")
#     if split_data[0] == "Add":
#         piece, composer, key = split_data[1:]
#         all_names = [p.name for p in pieces]
#         if piece in all_names:
#             print(f"{piece} is already in the collection!")
#         else:
#             new_piece = Piece(piece, composer, key)
#             pieces.append(new_piece)
#             print(f"{piece} by {composer} in {key} added to the collection!")
#     elif split_data[0] == "Remove":
#         piece = split_data[1]
#         all_names = [p.name for p in pieces]
#         if piece in all_names:
#             piece_to_remove = [p for p in pieces if p.name == piece][0]
#             pieces.remove(piece_to_remove)
#             print(f"Successfully removed {piece}!")
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#
#     elif split_data[0] == "ChangeKey":
#         piece, new_key = split_data[1:]
#         all_names = [p.name for p in pieces]
#         if piece in all_names:
#             piece_to_change = [p for p in pieces if p.name == piece][0]
#             piece_to_change.key = new_key
#             print(f"Changed the key of {piece} to {new_key}!")
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#     data = input()
#
# sorted_pieces = sorted(pieces, key=lambda p: (p.name, p.composer))
#
# for piece in sorted_pieces:
#     print(f"{piece.name} -> Composer: {piece.composer}, Key: {piece.key}")
