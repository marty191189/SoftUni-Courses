class Programmer:

    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = int(skills)

    def watch_course(self, course_name, language, skills_earned):

        if self.language == language:
            self.skills += int(skills_earned)
            return f"{self.name} watched {course_name}"

        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):

        if self.skills >= int(skills_needed) and not self.language == new_language:
            result = f"{self.name} switched from {self.language} to {new_language}"
            self.language = new_language
            return result

        elif self.skills >= int(skills_needed) and self.language == new_language:
            return f"{self.name} already knows {self.language}"

        elif self.skills < int(skills_needed):
            return f"{self.name} needs {abs(self.skills - skills_needed)} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
