s = input()
d, res = 1, 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        ++d
        print(d)
    else:
        print(s[i], s[i - 1])
        res = max(res, d)
        d = 1
print(max(res, d))