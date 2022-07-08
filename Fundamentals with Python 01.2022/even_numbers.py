numbers = input().split(", ")
numbers = list(map(int, numbers))
index_even_numbers = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        index_even_numbers.append(i)

print(index_even_numbers)
