letter = None

etaji = int(input())                       # number of levels in the building
rooms = int(input())

for etaj in range(etaji, 0, -1):
    for room in range(0, rooms):
        if etaj % 2 == 0:
            letter = "O"

        else:
            letter = "A"

        if etaj == etaji:
            letter = "L"

        print(f"{letter}{etaj}{room}", end=" ")

    print()
