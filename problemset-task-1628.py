import sys

input = sys.stdin.buffer.read
write = sys.stdout.write
data = input().split()

n, x = map(int, data[0 : 2])
t = list(map(int, data[2 : 2 + n]))

