import os

result_dict = {}

for root, dirs, files in os.walk("./"):

    for file in files:
        ext = file.split(".")[-1]

        if ext not in result_dict:
            result_dict[ext] = []

        result_dict[ext].append(file)

with open("./report.txt", "w") as output_file:

    for ext, files in result_dict.items():
        output_file.write('.' + ext + '\n')

        for file in files:
            output_file.write(f"- - - {file}\n")


# втори начин
#
# import os
#
#
# def directory_traversal(path, files_by_ext_dict):
#
#     for element in os.listdir(path):
#
#         if os.path.isdir(os.path.join(path, element)):
#             directory_traversal(os.path.join(path, element), files_by_ext_dict)
#
#         else:
#             extension = element.split(".")[-1]
#
#             if extension not in files_by_ext_dict:
#                 files_by_ext_dict[extension] = []
#
#             files_by_ext_dict[extension].append(element)
#
#
# result_dict = {}
#
# directory_traversal('./', result_dict)
#
# with open("./report.txt", "w") as output_file:
#
#     for ext, files in result_dict.items():
#         output_file.write('.' + ext + '\n')
#
#         for file in files:
#             output_file.write(f"- - - {file}\n")
