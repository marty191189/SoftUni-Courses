text = input().split("|")

result_list = []

for index in range(len(text) - 1, -1, -1):
    current_el = text[index].strip().split()
    result_list.extend(current_el)

print(' '.join(result_list))
