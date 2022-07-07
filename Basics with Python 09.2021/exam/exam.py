number_of_students = int(input())

counter_5_or_more = 0
counter_4_to_5 = 0
counter_3_to_4 = 0
counter_2_to_3 = 0

all_grades = 0
average = 0

for student in range(1, number_of_students + 1):
    current_grade = float(input())

    if 5.00 <= current_grade:
        counter_5_or_more += 1
        all_grades += current_grade

    elif 4.00 <= current_grade <= 4.99:
        counter_4_to_5 += 1
        all_grades += current_grade

    elif 3.00 <= current_grade <= 3.99:
        counter_3_to_4 += 1
        all_grades += current_grade

    elif current_grade < 3.00:
        counter_2_to_3 += 1
        all_grades += current_grade

percent_5_or_more = (counter_5_or_more / number_of_students) * 100
percent_4_to_5 = (counter_4_to_5 / number_of_students) * 100
percent_3_to_4 = (counter_3_to_4 / number_of_students) * 100
percent_2_to_3 = (counter_2_to_3 / number_of_students) * 100

average = all_grades / number_of_students

print(f"Top students: {percent_5_or_more:.2f}%")
print(f"Between 4.00 and 4.99: {percent_4_to_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_3_to_4:.2f}%")
print(f"Fail: {percent_2_to_3:.2f}%")
print(f"Average: {average:.2f}")
