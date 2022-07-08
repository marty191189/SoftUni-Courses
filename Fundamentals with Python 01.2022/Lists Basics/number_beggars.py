money_list = input().split(", ")
beggars_number = int(input())

beggars_list = []
offers_counter = 0

for i in range(beggars_number):
    beggars_list.append(0)

while offers_counter < len(money_list):
    for j in range(len(beggars_list)):
        if offers_counter >= len(money_list):
            break

        beggars_list[j] += int(money_list[offers_counter])
        offers_counter += 1


print(beggars_list)

# втори начин

# sums = input().split(", ")
# sums_int = list(map(int, sums))
# beggars = int(input())
# earn = []
#
# for i in range(beggars):
#     total = [sums_int[i] for i in range(i, len(sums_int), beggars)]
#     money = sum(total)
#     earn.append(money)
#
# print(earn)
