def find_sum(*args):

    negative_sum = 0
    positive_sum = 0

    for num in args:

        if num >= 0:
            positive_sum += num

        else:
            negative_sum += num

    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")

    return


nums_list = [int(el) for el in input().split()]

find_sum(*nums_list)
