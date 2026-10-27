import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
x = int(data[1])
c = [int(data[i]) for i in range(2, 2 + n)]

print(n, x, c)