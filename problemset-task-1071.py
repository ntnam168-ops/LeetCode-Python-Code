t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x == y:
        print(x * y)
    elif x > y:
        print((x - 1) ** 2 + y if x & 1 else x ** 2 - y + 1)
    elif x < y:
        print(y ** 2 - x + 1 if y & 1 else (y - 1) ** 2 + x)