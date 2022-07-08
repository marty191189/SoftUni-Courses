num = input()
res = [int(x) for x in str(num)]
res.sort(reverse=True)
print(*res, sep='')
