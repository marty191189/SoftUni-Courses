username = input()
password = input()
current_pass = ''

while current_pass != password:
    current_pass = input()

    if current_pass == password:
        break

print(f"Welcome {username}!")
