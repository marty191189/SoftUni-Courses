file_path = input().split(chr(92))

data = file_path[-1]

data = data.split(".")

file_name = data[0]
file_extension = data[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")

# втори начин
#
# file_path = input().split(chr(92))
#
# data = file_path[-1]
#
# data = data.split(".")
#
# result_dict = {}
#
# file_name = data[0]
# file_extension = data[1]
#
# result_dict[file_name] = file_extension
#
# for key, value in result_dict.items():
#     print(f"File name: {key}\nFile extension: {value}")

# трети начин
#
# def extract_file(data):
#     needed_information = data[-1].split(".")
#
#     file_name = needed_information[0]
#     extension = needed_information[1]
#
#     print(f"File name: {file_name}")
#     print(f"File extension: {extension}")
#
#
# data_1 = input().split("\\")
# extract_file(data_1)
