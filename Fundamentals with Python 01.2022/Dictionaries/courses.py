command = input()

courses_dict = {}

while not command == "end":

    data = command.split(" : ")

    course_name = data[0]
    student_name = data[1]

    if course_name not in courses_dict:
        courses_dict[course_name] = []
        courses_dict[course_name].append(student_name)

    else:
        courses_dict[course_name].append(student_name)

    command = input()

for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")

    for name in value:
        print(f"-- {''.join(name)}")
