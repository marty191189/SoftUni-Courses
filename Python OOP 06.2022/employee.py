class Employee:

    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def get_full_name(self):
        result = f"{self.first_name} {self.last_name}"
        return result

    def get_annual_salary(self):
        result = self.salary * 12
        return result

    def raise_salary(self, amount: int):
        self.salary += int(amount)
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
