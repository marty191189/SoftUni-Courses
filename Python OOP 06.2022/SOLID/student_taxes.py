class StudentTaxes:

    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4


class AdditionalDiscount(StudentTaxes):

    def get_discount(self):

        result = super().get_discount()

        if result:
            return result

        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2


student_1 = AdditionalDiscount("Ana", 1000, 5.5)
student_2 = AdditionalDiscount("Ivan", 1000, 3)
student_3 = AdditionalDiscount("George", 1000, 4.5)

print(student_1.get_discount())
print(student_2.get_discount())
print(student_3.get_discount())
