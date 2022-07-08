my_gifts = input().split(' ')
actions = input()
while actions != 'No Money':
    commands = actions.split(' ')
    command = commands[0]
    gift = commands[1]

    if command == 'OutOfStock':
        for i in range(len(my_gifts)):
            if my_gifts[i] == gift:
                my_gifts[i] = "None"

    elif command == 'Required':
        index = int(commands[2])

        if 0 <= index < len(my_gifts):
            my_gifts[index] = gift

    elif command == 'JustInCase':
        my_gifts[-1] = gift

    actions = input()

my_gifts = [x for x in my_gifts if x != 'None']
my_gifts = ' '.join(my_gifts)
print(my_gifts)
