number_of_students = int(input())

student_dict = {}

for student in range(1, number_of_students + 1):

    student_data = input().split()
    student_name = student_data[0]
    student_grade = float(student_data[1])

    if student_name not in student_dict:
        student_dict[student_name] = []
    student_dict[student_name].append(student_grade)

for data in student_dict.items():
    print(f"{data[0]} -> {' '.join([f'{el:.2f}' for el in data[1]])} (avg: {sum(data[1])/len(data[1]):.2f})")
