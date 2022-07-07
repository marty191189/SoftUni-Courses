name_of_student = input()

sum_all_grades = 0
all_grades_counter = 0
average_grade = 0

bad_grade_counter = 0
class_counter = 0

while True:
    grade = float(input())

    if 4 <= grade:
        sum_all_grades += grade
        all_grades_counter += 1

        if all_grades_counter == 12:
            average_grade = sum_all_grades / all_grades_counter
            print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
            break
    else:
        bad_grade_counter += 1

        if 2 <= bad_grade_counter:
            print(f"{name_of_student} has been excluded at {class_counter} grade")
            break

    class_counter += 1
