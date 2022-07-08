number_of_chars = int(input())

total_sum = 0

for number in range(1, number_of_chars + 1):
    current_char = input()
    current_ascii_sum = ord(current_char)

    total_sum += current_ascii_sum

print(f"The sum equals: {total_sum}")
