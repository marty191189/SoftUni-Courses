len_first_set, len_second_set = [int(el) for el in input().split()]

n_set = set()
m_set = set()

for n in range(1, len_first_set + 1):
    current_number = int(input())
    n_set.add(current_number)

for m in range(1, len_second_set + 1):
    current_number = int(input())
    m_set.add(current_number)

unique_set = n_set.intersection(m_set)

print("\n".join([str(el) for el in unique_set]))
