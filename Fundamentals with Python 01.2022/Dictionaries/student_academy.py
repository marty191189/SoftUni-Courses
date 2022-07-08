number_of_lines = int(input())

grades_dict = {}

average_grade = 0

for number in range(1, number_of_lines + 1):
    student_name = input()
    current_grade = float(input())

    if student_name not in grades_dict:
        grades_dict[student_name] = []
        grades_dict[student_name].append(current_grade)

    else:
        grades_dict[student_name].append(current_grade)

for key, value in grades_dict.items():
    average_grade = sum(value) / len(value)

    if average_grade >= 4.50:
        print(f"{key} -> {average_grade:.2f}")
