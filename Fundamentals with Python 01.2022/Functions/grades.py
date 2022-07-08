grade = float(input())


def grade_as_text(number):
    if 2 <= number <= 2.99:
        print("Fail")

    elif 3 <= number <= 3.49:
        print("Poor")

    elif 3.50 <= number <= 4.49:
        print("Good")

    elif 4.50 <= number <= 5.49:
        print("Very Good")

    elif 5.50 <= number <= 6:
        print("Excellent")


grade_as_text(grade)

# втори начин

# grade = float(input())
#
#
# def grade_as_text(number):
#     if 2 <= number <= 2.99:
#         return "Fail"
#
#     elif 3 <= number <= 3.49:
#         return "Poor"
#
#     elif 3.50 <= number <= 4.49:
#         return "Good"
#
#     elif 4.50 <= number <= 5.49:
#         return "Very Good"
#
#     elif 5.50 <= number <= 6:
#         return "Excellent"
#
#
# print(grade_as_text(grade))


# трети начин

# def grade_as_text():
#
#     grade = float(input())
#
#     if 2 <= grade <= 2.99:
#         return "Fail"
#
#     elif 3 <= grade <= 3.49:
#         return "Poor"
#
#     elif 3.50 <= grade <= 4.49:
#         return "Good"
#
#     elif 4.50 <= grade <= 5.49:
#         return "Very Good"
#
#     elif 5.50 <= grade <= 6:
#         return "Excellent"
#
#
# print(grade_as_text())
# print(grade_as_text())
# print(grade_as_text())
# мога да принтирам/използвам функцията няколко пъти(пусни, за да видиш)
