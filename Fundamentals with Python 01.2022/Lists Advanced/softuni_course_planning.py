lessons_list = input().split(", ")

swap_done = False

data = input()

while not data == "course start":

    data = data.split(":")

    command = data[0]

    if command == "Add":
        lesson_title = data[1]

        if lesson_title not in lessons_list:
            lessons_list.append(lesson_title)

    elif command == "Insert":
        lesson_title = data[1]
        index = int(data[2])

        if lesson_title not in lessons_list:
            lessons_list.insert(index, lesson_title)

    elif command == "Remove":
        lesson_title = data[1]
        exercise_title = f"{lesson_title}-Exercise"

        if lesson_title in lessons_list:
            lessons_list.remove(lesson_title)
        if exercise_title in lessons_list:
            lessons_list.remove(exercise_title)

    elif command == "Swap":
        old_lesson_title = data[1]
        new_lesson_title = data[2]

        old_exercise_title = f"{old_lesson_title}-Exercise"
        new_exercise_title = f"{new_lesson_title}-Exercise"

        if old_lesson_title in lessons_list and new_lesson_title in lessons_list:
            old_lesson_index = int(lessons_list.index(old_lesson_title))
            new_lesson_index = int(lessons_list.index(new_lesson_title))
            lessons_list[old_lesson_index], lessons_list[new_lesson_index] = lessons_list[new_lesson_index], \
                                                                             lessons_list[old_lesson_index]

            if old_exercise_title in lessons_list and new_exercise_title in lessons_list:
                new_exercise_title_index = lessons_list.index(new_exercise_title)
                popped_lesson = lessons_list.pop(new_exercise_title_index)
                lessons_list.insert(old_lesson_index + 1, popped_lesson)

                old_exercise_title_index = lessons_list.index(old_exercise_title)
                popped_lesson = lessons_list.pop(old_exercise_title_index)
                lessons_list.insert(new_lesson_index + 1, popped_lesson)

                swap_done = True

            if not swap_done:
                if new_exercise_title in lessons_list:
                    new_exercise_title_index = lessons_list.index(new_exercise_title)
                    popped_lesson = lessons_list.pop(new_exercise_title_index)
                    lessons_list.insert(old_lesson_index + 1, popped_lesson)

    elif command == "Exercise":
        lesson_title = data[1]

        if lesson_title in lessons_list:
            exercise_title = f"{lesson_title}-Exercise"

            if exercise_title not in lessons_list:
                lesson_index = int(lessons_list.index(lesson_title))
                lessons_list.insert(lesson_index + 1, exercise_title)

        elif lesson_title not in lessons_list:
            lessons_list.append(lesson_title)
            exercise_title = f"{lesson_title}-Exercise"
            lessons_list.append(exercise_title)

    swap_done = False

    data = input()

for index in range(0, len(lessons_list)):
    print(f"{index + 1}.{lessons_list[index]}")
