number_of_students = int(input())
p5_or_more = 0
p4_to_5 = 0
p3_to_4 = 0
p2_to_3 = 0

average_grade = 0
student_grade = 0
grade_for_average = 0

for student in range(number_of_students):
    student_grade = float(input())
    grade_for_average += student_grade

    if student_grade < 3:
        p2_to_3 += 1

    elif 3 <= student_grade <= 3.99:
        p3_to_4 += 1

    elif 4 <= student_grade <= 4.99:
        p4_to_5 += 1

    elif 5 <= student_grade:
        p5_or_more += 1

final_p5_or_more = ((p5_or_more / number_of_students) * 100)
final_p4_to_5 = ((p4_to_5 / number_of_students) * 100)
final_p3_to_4 = ((p3_to_4 / number_of_students) * 100)
final_p2_to_3 = ((p2_to_3 / number_of_students) * 100)

average_grade = grade_for_average / number_of_students

print(f"Top students: {final_p5_or_more:.2f}%")
print(f"Between 4.00 and 4.99: {final_p4_to_5:.2f}%")
print(f"Between 3.00 and 3.99: {final_p3_to_4:.2f}%")
print(f"Fail: {final_p2_to_3:.2f}%")
print(f"Average: {average_grade:.2f}")
