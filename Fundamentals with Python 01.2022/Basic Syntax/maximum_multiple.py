divisor = int(input())
boundary = int(input())

max_i = 0

for i in range(1, boundary + 1):

    if i % divisor == 0 and i <= boundary:
        max_i = i

print(max_i)

# втори начин
#
# first_number = int(input())
# second_number = int(input())
#
# result = int(second_number / first_number) * first_number
#
# print(result)
