a = float(input())
result = None

while 0 <= a:
    result = a * 2
    print(f"Result: {result:.2f}")
    a = float(input())
    if a < 0:
        print("Negative number!")
        break
