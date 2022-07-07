n = int(input())
left_sum = 0
right_sum = 0

for number in range(1, n+1):
    num1 = int(input())
    left_sum += num1

for number in range(1, n+1):
    num1 = int(input())
    right_sum += num1

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")

else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
