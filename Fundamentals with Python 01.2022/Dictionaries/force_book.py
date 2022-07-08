def create_force_side(side, member, user_info_dict):
    condition = [current_side for current_side in user_info_dict if member in user_info_dict[current_side]]

    if len(condition) == 0:
        condition.clear()
        if side not in user_info_dict:
            user_info_dict[side] = [member]
        else:
            user_info_dict[side].append(member)

    return user_info_dict


def create_force_user(member, side, user_info_dict):
    for current_side in user_info_dict:
        if member in user_info_dict[current_side]:
            if len(user_info_dict[current_side]) > 1:
                user_info_dict[current_side].pop(member)
                break
            else:
                del user_info_dict[current_side]
                break

    if side in user_info_dict:
        user_info_dict[side].append(member)
    else:
        user_info_dict[side] = [member]

    print(f"{member} joins the {side} side!")


def force_book():
    user_info_dict = {}

    while True:
        command = input()

        if command == 'Lumpawaroo':
            break

        if '|' in command:
            command = command.split(' | ')
            side = command[0]
            member = command[1]
            create_force_side(side, member, user_info_dict)

        elif '->' in command:
            command = command.split(' -> ')
            member = command[0]
            side = command[1]
            create_force_user(member, side, user_info_dict)

    for data in user_info_dict:
        print(f'Side: {data}, Members: {len(user_info_dict[data])}')
        for name in user_info_dict[data]:
            print(f'! {name}')


force_book()


# втори начин
#
# def force_user_exists(force_book_dict: dict, user: str):
#     for user_list in force_book_dict.values():
#         if user in user_list:
#             return True
#
#     return False
#
#
# def remove_user_from_side(force_book_dict: dict, user: str):
#     for (side, users) in force_book_dict.items():
#         if user in users:
#             force_book_dict[side].remove(user)
#
#
# def initial_join_force_side(force_book_dict: dict, side: str, user: str):
#     if side not in force_book_dict.keys() and not force_user_exists(force_book_dict, user):
#         force_book_dict[side] = []
#         force_book_dict[side].append(user)
#     elif not force_user_exists(force_book_dict, user):
#         force_book_dict[side].append(user)
#
#
# def join_force_side(force_book_dict: dict, side: str, user: str):
#     if side not in force_book_dict.keys() and not force_user_exists(force_book_dict, user):
#         force_book_dict[side] = []
#         force_book_dict[side].append(user)
#     elif not force_user_exists(force_book_dict, user):
#         if side not in force_book_dict.keys():
#             force_book_dict[side] = []
#         force_book_dict[side].append(user)
#     elif force_user_exists(force_book_dict, user):
#         remove_user_from_side(force_book_dict, user)
#
#         if side not in force_book_dict.keys():
#             force_book_dict[side] = []
#
#         force_book_dict[side].append(user)
#
#     print(f'{user} joins the {side} side!')
#
#
# force_book = {}
#
# command = input()
# while command != 'Lumpawaroo':
#     if '|' in command:
#         cmd_info = command.split(' | ')
#         force_side = cmd_info[0]
#         force_user = cmd_info[1]
#
#         initial_join_force_side(force_book, force_side, force_user)
#     elif '->' in command:
#         cmd_info = command.split(' -> ')
#         force_user = cmd_info[0]
#         force_side = cmd_info[1]
#
#         join_force_side(force_book, force_side, force_user)
#
#     command = input()
#
# for (side, users) in force_book.items():
#     if len(users) > 0:
#         print(f'Side: {side}, Members: {len(users)}')
#
#         for user in users:
#             print(f'! {user}')


# трети начин - накрая принта е сортиран
#
# def force_user_exists(force_book_dict: dict, user: str):
#     for user_list in force_book_dict.values():
#         if user in user_list:
#             return True
#
#     return False
#
#
# def remove_user_from_side(force_book_dict: dict, user: str):
#     for (side, users) in force_book_dict.items():
#         if user in users:
#             force_book_dict[side].remove(user)
#
#
# def initial_join_force_side(force_book_dict: dict, side: str, user: str):
#     if side not in force_book_dict.keys() and not force_user_exists(force_book_dict, user):
#         force_book_dict[side] = []
#         force_book_dict[side].append(user)
#     elif not force_user_exists(force_book_dict, user):
#         force_book_dict[side].append(user)
#
#
# def join_force_side(force_book_dict: dict, side: str, user: str):
#     if side not in force_book_dict.keys() and not force_user_exists(force_book_dict, user):
#         force_book_dict[side] = []
#         force_book_dict[side].append(user)
#     elif not force_user_exists(force_book_dict, user):
#         if side not in force_book_dict.keys():
#             force_book_dict[side] = []
#         force_book_dict[side].append(user)
#     elif force_user_exists(force_book_dict, user):
#         remove_user_from_side(force_book_dict, user)
#
#         if side not in force_book_dict.keys():
#             force_book_dict[side] = []
#
#         force_book_dict[side].append(user)
#
#     print(f'{user} joins the {side} side!')
#
#
# force_book = {}
#
# command = input()
# while command != 'Lumpawaroo':
#     if '|' in command:
#         cmd_info = command.split(' | ')
#         force_side = cmd_info[0]
#         force_user = cmd_info[1]
#
#         initial_join_force_side(force_book, force_side, force_user)
#     elif '->' in command:
#         cmd_info = command.split(' -> ')
#         force_user = cmd_info[0]
#         force_side = cmd_info[1]
#
#         join_force_side(force_book, force_side, force_user)
#
#     command = input()
#
# for (side, users) in sorted(force_book.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
#     if len(users) > 0:
#         print(f'Side: {side}, Members: {len(users)}')
#
#         for user in sorted(users):
#             print(f'! {user}')
