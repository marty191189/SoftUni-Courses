number_of_judges = int(input())
name_of_presentation = input()

sum_grades_for_presentation = 0
average_grade = 0
sum_average_grade = 0
number_of_presentations = 0

while name_of_presentation != "Finish":

    number_of_presentations += 1

    for judge in range(1, number_of_judges + 1):
        current_grade = float(input())
        sum_grades_for_presentation += current_grade
        average_grade = sum_grades_for_presentation / number_of_judges

    print(f"{name_of_presentation} - {average_grade:.2f}.")

    sum_average_grade += average_grade

    sum_grades_for_presentation = 0
    average_grade = 0
    name_of_presentation = input()

final_assessment = sum_average_grade / number_of_presentations
print(f"Student's final assessment is {final_assessment:.2f}.")
