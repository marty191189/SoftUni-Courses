nums = [int(el) for el in input().split()]
factor = int(input())

happiness = [el * factor for el in nums]

border_line = sum(happiness) / len(happiness)

happy_employees = [el for el in happiness if el >= border_line]
sad_employees = [el for el in happiness if el < border_line]

happy_message = "Employees are happy!"
sad_message = "Employees are not happy!"

if len(sad_employees) > len(happiness) / 2:
    print(f"Score: {len(happy_employees)}/{(len(happiness))}. {sad_message}")

else:
    print(f"Score: {len(happy_employees)}/{(len(happiness))}. {happy_message}")

# втори начин

# employees = input().split(" ")
# employees = list(map(int, employees))
# factor = int(input())
#
# happy_employees = list(filter(lambda emp: emp >= sum(employees) / len(employees), employees))
#
# if len(happy_employees) >= (len(employees) / 2):
#     print(f"Score: {len(happy_employees)}/{(len(employees))}. Employees are happy!")
#
# else:
#     print(f"Score: {len(happy_employees)}/{(len(employees))}. Employees are not happy!")
