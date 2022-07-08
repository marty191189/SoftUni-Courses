def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key=lambda kvp_tuple: (-len(kvp_tuple[1]), kvp_tuple[0]))

    result = ""

    for name, quantity in sorted_cheese:
        result += name + '\n'
        quantity_as_str = [str(el) for el in sorted(quantity, reverse=True)]
        result += '\n'.join(quantity_as_str) + '\n'

    return result
