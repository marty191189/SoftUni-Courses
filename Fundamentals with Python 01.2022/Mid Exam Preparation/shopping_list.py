def is_item_in_groceries(groceries_list, item):
    if item in groceries_list:
        return True
    return False


groceries = input().split("!")

data = input()

while not data == "Go Shopping!":
    command_data = data.split()
    if command_data[0] == "Urgent":
        item = command_data[1]
        if not is_item_in_groceries(groceries, item):
            groceries.insert(0, item)
    elif command_data[0] == "Unnecessary":
        item = command_data[1]
        if is_item_in_groceries(groceries, item):
            groceries.remove(item)
    elif command_data[0] == "Correct":
        old_tem = command_data[1]
        new_item = command_data[2]
        if is_item_in_groceries(groceries, old_tem):
            index = groceries.index(old_tem)
            groceries[index] = new_item
    elif command_data[0] == "Rearrange":
        item = command_data[1]
        if is_item_in_groceries(groceries, item):
            groceries.remove(item)
            groceries.append(item)
    data = input()

print(", ".join(groceries))
