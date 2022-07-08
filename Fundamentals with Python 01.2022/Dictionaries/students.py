data = input()
courses = {}

while ":" in data:

    student_name, student_id, course_name = data.split(":")
    # data = data.split(":")
    # student_name = data[0]
    # student_id = data[1]
    # course_name = data[2]

    if course_name not in courses:
        courses[course_name] = {}
    courses[course_name][student_id] = student_name

    data = input()

searched_course = data
searched_course_name_as_list = searched_course.split("_")
searched_course = ' '.join(searched_course_name_as_list)

# data.replace("_", " ")

for course_name in courses:
    if course_name == searched_course:
        for student_id, name in courses[course_name].items():
            print(f"{name} - {student_id}")
