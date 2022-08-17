# първи начин
#
# from collections import deque
#
# pizzas_deque = deque([int(el) for el in input().split(", ") if 0 < int(el) < 11])
#
# employees_stack = [int(el) for el in input().split(", ")]
#
# total_pizzas_made = 0
#
# is_finished = False
#
# while pizzas_deque and employees_stack:
#
#     while employees_stack[-1] < pizzas_deque[0]:
#         total_pizzas_made += employees_stack[-1]
#         pizzas_deque[0] = pizzas_deque[0] - employees_stack[-1]
#         employees_stack.pop()
#
#         if not pizzas_deque or not employees_stack:
#             is_finished = True
#             break
#
#     if is_finished:
#         break
#
#     total_pizzas_made += pizzas_deque.popleft()
#     employees_stack.pop()
#
# if pizzas_deque:
#     print("Not all orders are completed.")
#     print(f"Orders left: {', '.join([str(el) for el in pizzas_deque])}")
#
# else:
#     print("All orders are successfully completed!")
#     print(f"Total pizzas made: {total_pizzas_made}")
#     print(f"Employees: {', '.join([str(el) for el in employees_stack])}")

# втори начин

from collections import deque


def make_pizzas(pizzas, employees):

    counter_pizzas = 0

    while pizzas and employees:

        while employees[-1] < pizzas[0]:
            counter_pizzas += employees[-1]
            pizzas[0] = pizzas[0] - employees[-1]
            employees.pop()

            if not pizzas or not employees:
                return

        counter_pizzas += pizzas.popleft()
        employees.pop()

    return counter_pizzas


pizzas_deque = deque([int(el) for el in input().split(", ") if 0 < int(el) < 11])

employees_stack = [int(el) for el in input().split(", ")]

total_pizzas_made = make_pizzas(pizzas_deque, employees_stack)

if pizzas_deque:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizzas_deque])}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join([str(el) for el in employees_stack])}")
