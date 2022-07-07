number_permitted_bad_grades = int(input())
bad_grades = 0
is_expelled = False
total_tasks = 0
average_grade = 0
last_task = ''
current_task = input()

while current_task != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1

        if bad_grades == number_permitted_bad_grades:
            is_expelled = True
            break

    average_grade += current_grade
    total_tasks += 1
    last_task = current_task

    current_task = input()

if is_expelled:
    print(f"You need a break, {number_permitted_bad_grades} poor grades.")
else:
    average_grade /= total_tasks
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_tasks}")
    print(f"Last problem: {last_task}")
