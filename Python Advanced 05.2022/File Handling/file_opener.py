# try:
#     file = open("text.txt", "r")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")

import os

if os.path.exists("text.txt"):
    print("File found")
else:
    print("File not found")
