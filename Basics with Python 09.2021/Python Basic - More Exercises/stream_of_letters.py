a = input()

counter_c = 0
counter_o = 0
counter_n = 0

word = ""

while a != "End":
    z = ord(a)

    if 65 <= z <= 90:

        if a == "c":
            counter_c += 1

            if counter_c >= 2:
                word += a

        elif a == "o":
            counter_o += 1

            if counter_o >= 2:
                word += a

        elif a == "n":
            counter_n += 1

            if counter_n >= 2:
                word += a

        else:
            word += a

        if counter_c >= 1:
            if counter_o >= 1:
                if counter_n >= 1:
                    print(f"{word}", end=" ")
                    counter_c = 0
                    counter_o = 0
                    counter_n = 0
                    word = ""

    elif 97 <= z <= 122:

        if a == "c":
            counter_c += 1

            if counter_c >= 2:
                word += a

        elif a == "o":
            counter_o += 1

            if counter_o >= 2:
                word += a

        elif a == "n":
            counter_n += 1

            if counter_n >= 2:
                word += a

        else:
            word += a

        if counter_c >= 1:
            if counter_o >= 1:
                if counter_n >= 1:
                    print(f"{word}", end=" ")
                    counter_c = 0
                    counter_o = 0
                    counter_n = 0
                    word = ""

    a = input()
