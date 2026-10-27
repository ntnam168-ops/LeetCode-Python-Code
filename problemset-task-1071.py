t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    d = max(x, y)
    d **= 2
    print(d)