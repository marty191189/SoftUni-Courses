from collections import deque

bowls_of_ramen_stack = [int(el) for el in input().split(", ")]
customers_deque = deque([int(el) for el in input().split(", ")])

while True:

    if not bowls_of_ramen_stack:
        break

    if not customers_deque:
        break

    current_bow = bowls_of_ramen_stack.pop()
    current_customer = customers_deque.popleft()

    if current_bow == current_customer:
        continue

    elif current_bow > current_customer:
        current_bow -= current_customer
        bowls_of_ramen_stack.append(current_bow)

    elif current_bow < current_customer:
        current_customer -= current_bow
        customers_deque.appendleft(current_customer)

if not customers_deque:
    print("Great job! You served all the customers.")

    if bowls_of_ramen_stack:
        print(f"Bowls of ramen left: {', '.join([str(el) for el in bowls_of_ramen_stack])}")

elif not bowls_of_ramen_stack:
    print("Out of ramen! You didn't manage to serve all customers.")

    if customers_deque:
        print(f"Customers left: {', '.join([str(el) for el in customers_deque])}")
