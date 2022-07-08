def grocery_store(**kwargs):

    sorted_receipt_list = sorted(kwargs.items(), key=lambda kvp_tpl: (-kvp_tpl[1], -len(kvp_tpl[0]), kvp_tpl[0]))

    result_list = []

    for kvp_tuple in sorted_receipt_list:
        current_string = f"{kvp_tuple[0]}: {kvp_tuple[1]}"
        result_list.append(current_string)

    return "\n".join(result_list)


print(grocery_store(bread=5, pasta=12, eggs=12))

print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1))
