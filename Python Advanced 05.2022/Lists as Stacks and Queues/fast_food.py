from collections import deque

total_food = int(input())
orders_queue = deque([int(el) for el in input().split()])

biggest_order = max(orders_queue)

print(biggest_order)

while total_food > 0 and orders_queue:

    current_order = orders_queue[0]

    if total_food >= current_order:
        total_food -= current_order
        orders_queue.popleft()

    else:
        break

if orders_queue:
    orders_queue_str = [str(num) for num in orders_queue]
    print(f"Orders left: {' '.join(orders_queue_str)}")
else:
    print("Orders complete")
