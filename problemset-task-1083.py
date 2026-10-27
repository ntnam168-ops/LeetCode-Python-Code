n = int(input())
ar = list(map(int, input().split()))
ar.sort()
for i in range(n - 1):
    if ar[i] != i + 1:
        print(i + 1)
        exit(0)
print(n)