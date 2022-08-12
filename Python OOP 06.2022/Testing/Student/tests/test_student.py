from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    STUDENT_NAME = "George"

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        courses = {"Python OOP": ["note_1", "note_2"]}
        student = Student(self.STUDENT_NAME, courses)

        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_student_updates_course_notes_when_course_is_already_enrolled(self):
        course_name = "Python OOP"
        courses = {course_name: ["note_1", "note_2"]}

        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ["note_3", "note_4"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note_1", "note_2", "note_3", "note_4"], student.courses[course_name])

    def test_enroll_student_extends_courses_with_notes_when_add_course_notes_is_not_passed(self):
        course_name = "Python OOP"
        course_notes = ["note_1", "note_2"]

        result = self.student.enroll(course_name, course_notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_notes_when_add_course_notes_is_y(self):
        course_name = "Python OOP"
        course_notes = ["note_1", "note_2"]

        result = self.student.enroll(course_name, course_notes, "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_without_notes_when_invalid_course_notes_argument_is_passed(self):
        course_name = "Python OOP"
        course_notes = ["note_1", "note_2"]

        result = self.student.enroll(course_name, course_notes, "N")

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes_raises_error_when_course_is_not_existing(self):

        with self.assertRaises(Exception) as exception:
            self.student.add_notes("Python OOP", "note_3")
        self.assertEqual("Cannot add notes. Course not found.", str(exception.exception))

    def test_add_notes_updates_course_notes_when_course_exists(self):
        course_name = "Python OOP"
        courses = {course_name: ["note_1", "note_2"]}

        student = Student(self.STUDENT_NAME, courses)

        result = student.add_notes(course_name, "note_3")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note_1", "note_2", "note_3"], student.courses[course_name])

    def test_leave_course_raises_error_when_course_is_not_existing(self):
        self.student.enroll("Python Fundamentals", [])

        with self.assertRaises(Exception) as exception:
            self.student.leave_course("Python OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(exception.exception))

    def test_leave_course_removes_course_when_student_is_enrolled_for_the_course(self):
        course_name = "Python Basics"
        student = Student(self.STUDENT_NAME, {course_name: []})

        result = student.leave_course(course_name)

        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in student.courses)


if __name__ == "__main__":
    main()
