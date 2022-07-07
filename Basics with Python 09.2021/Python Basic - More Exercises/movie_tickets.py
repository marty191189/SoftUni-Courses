a1 = int(input())
a2 = int(input())
n = int(input())
p = int(n / 2)

for s1 in range(a1, a2):
    for s2 in range(1, n):
        for s3 in range(1, p):
            if s1 % 2 != 0:
                if (s2 + s3 + s1) % 2 != 0:
                    print(f"{chr(s1)}-{s2}{s3}{s1}")
