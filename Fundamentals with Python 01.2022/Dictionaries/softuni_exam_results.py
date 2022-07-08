#
#
# # втори начин
# #
# class ExamResults:
#     results, banned = {}, None
#
#     def __init__(self, username, language, points):
#         self.userdict, self.username, self.language, self.points = {username: points}, username, language, points
#
#     def add_result(self):
#         if self.language != 'banned':
#             if self.language not in self.results:
#                 self.results[self.language] = self.userdict
#             elif self.username not in self.results[self.language]:
#                 self.results[self.language].update({self.username: self.points})
#             else:
#                 if self.results[self.language][self.username] < self.points:
#                     self.results[self.language][self.username] = self.points
#             try:
#                 self.results[self.language]['submissions'] += 1
#             except:
#                 self.results[self.language]['submissions'] = 1
#         else:
#             self.banned = self.username
#
#     def print_result(self):
#         print('Results:')
#         for language in self.results:
#             for student, score in self.results[language].items():
#                 if student != self.banned:
#                     if student != 'submissions':
#                         print(f'{student} | {score}')
#         print('Submissions:')
#         for language in self.results:
#             print(f"{language} - {self.results[language]['submissions']}")
#
#
# command = input()
# while command != 'exam finished':
#     command = command.split('-')
#     if command[1] != 'banned':
#         student_result = ExamResults(command[0], command[1], int(command[2]))
#     else:
#         student_result = ExamResults(command[0], command[1], 0)
#     student_result.add_result()
#     command = input()
# student_result.print_result()
