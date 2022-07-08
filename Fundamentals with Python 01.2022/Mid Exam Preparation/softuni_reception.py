first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

number_of_students = int(input())

counter_hours_needed = 0

students_helped_per_hour = first_employee + second_employee + third_employee

while number_of_students > 0:

    number_of_students -= students_helped_per_hour

    counter_hours_needed += 1

    if counter_hours_needed % 4 == 0:
        counter_hours_needed += 1

print(f"Time needed: {counter_hours_needed}h.")
