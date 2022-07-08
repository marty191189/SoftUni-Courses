product = input()
quantity = int(input())


def order(product_1, quantity_1):

    result = None

    if product_1 == "coffee":
        result = quantity_1 * 1.50

    elif product_1 == "coke":
        result = quantity_1 * 1.40

    elif product_1 == "water":
        result = quantity_1 * 1

    elif product_1 == "snacks":
        result = quantity_1 * 2

    return result


print(f"{order(product, quantity):.2f}")

# по-красиво и четливо

# final_price = order(product, quantity)
#
# print(f"{final_price:.2f}")
