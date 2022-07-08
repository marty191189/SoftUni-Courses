import string


def valid_username(text):
    flag = 0

    expected_elements = string.digits + string.ascii_letters + "-" + "_"

    for name in text:

        flag = 0

        if len(name) < 3 or len(name) > 16:
            flag = 1

        elif len([x for x in name if x in expected_elements]) != len(name):
            flag = 1

        elif flag == 0:
            print(name)


usernames = input().split(", ")

valid_username(usernames)

# втори начин
#
# usernames = input().split(", ")
#
# for username in usernames:
#     condition = username.isalnum() or "_" in username or "-" in username
#     if 3 <= len(username) <= 16 and condition:
#         print(username)
