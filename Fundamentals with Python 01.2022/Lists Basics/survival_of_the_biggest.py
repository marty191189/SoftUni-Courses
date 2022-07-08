numbers = input().split(" ")

count = int(input())

copy_numbers = list(map(int, numbers))

for i in range(1, count + 1):
    current_min_element = min(copy_numbers)
    numbers.remove(str(current_min_element))
    copy_numbers.remove(current_min_element)

print(", ".join(numbers))
