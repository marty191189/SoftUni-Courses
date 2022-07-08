
# втори начин Марио
#
# def additional_func(partition):
#     current_max_num = 0
#     special_char = ''
#
#     for ch in partition:
#         if ch != special_char:
#             if current_max_num >= 6:
#                 break
#             current_max_num = 1
#             special_char = ch
#         else:
#             current_max_num += 1
#     return [current_max_num, special_char]
#
# def ticket_validator(ticket):
#     ticket_condition = ''
#
#     if len(ticket) != 20:
#         ticket_condition = "invalid ticket"
#     elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
#         ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
#     else:
#         data_source = ''
#         if additional_func(ticket[0:10]) > additional_func(ticket[10:]):
#             data_source = additional_func(ticket[10:])
#         else:
#             data_source = additional_func(ticket[0:10])
#
#         number_of_special_signs = data_source[0]
#         special_sign = data_source[1]
#
#         if number_of_special_signs < 6 or special_sign not in '@#$^':
#             ticket_condition = f'ticket "{ticket}" - no match'
#         else:
#             ticket_condition = f'ticket "{ticket}" - {number_of_special_signs}{special_sign}'
#
#     return ticket_condition
#
# def winning_ticket(data):
#     for ticket in data:
#         print(ticket_validator(ticket))
#
#
# tickets_info = input()
# data = [x.strip() for x in tickets_info.split(',')]
# winning_ticket(data)


# трети начин Инес

# winning_symbols = ["@", "#", "$", "^"]
#
#
# def is_jackpot(ticket):
#     for winning_symbol in winning_symbols:
#         if winning_symbol in ticket:
#             if ticket.count(winning_symbol) == 20:
#                 print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
#                 return True
#     return False
#
#
# def is_winning_ticket(ticket):
#     left_half = ticket[:10]
#     right_half = ticket[10:]
#     for winning_symbol in winning_symbols:
#         if winning_symbol*6 in left_half and winning_symbol*6 in right_half:
#             left_symbols_count = left_half.count(winning_symbol)
#             right_symbols_count = right_half.count(winning_symbol)
#             match_result = min(left_symbols_count, right_symbols_count)
#             print(f"ticket \"{ticket}\" - {match_result}{winning_symbol}")
#             return True
#     return False
#
#
# tickets = [el.strip() for el in input().split(", ")]
#
# for ticket in tickets:
#     if not len(ticket) == 20:
#         print(f"invalid ticket")
#         continue
#     if is_jackpot(ticket):
#         continue
#
#     if is_winning_ticket(ticket):
#         continue
#
#     print(f"ticket \"{ticket}\" - no match")


# четвърти начин с RegEx
#
# from re import findall
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
#
# win = r"[\^]{6,10}|[\$]{6,10}|[\@]{6,10}|[\#]{6,10}"
# jackpot = r"[\^]{20}|[\$]{20}|[\@]{20}|[\#]{20}"
#
# for y in tickets:
#     if not len(y) == 20:
#         print("invalid ticket")
#         continue
#     else:
#         first_half = y[:10]
#         second_half = y[10:]
#         check_win_first = findall(win, first_half)
#         check_win_second = findall(win, second_half)
#         check_jackpot = findall(jackpot, y)
#         if check_jackpot:
#             print(f"ticket \"{y}\" - 10{y[0]} Jackpot!")
#         elif check_win_first and check_win_second:
#             length = min(len(check_win_first[0]), len(check_win_second[0]))
#             print(f"ticket \"{y}\" - {length}{check_win_first[0][0]}")
#         else:
#             print(f"ticket \"{y}\" - no match")
