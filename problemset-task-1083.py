n = int(input())
ar = list(map(int, input().split()))
for i in range(n):
    if ar[i] != i - 1:
        print(i)
        exit(0)