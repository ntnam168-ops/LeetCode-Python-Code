import sys

input = sys.stdin.read
data = input().split()

n = data[0]
x = data[1]
c = [int(x) for x in range(2, 2 + n)]