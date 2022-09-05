def create_seq(num):

    seq = [0, 1]

    for _ in range(3, num + 1):
        seq.append(seq[-1] + seq[-2])

    return seq


def locate(num_1, seq_1):

    if num_1 in seq_1:
        print(f"The number - {num_1} is at index {seq_1.index(num_1)}")

    else:
        print(f"The number {num_1} is not in the sequence")
