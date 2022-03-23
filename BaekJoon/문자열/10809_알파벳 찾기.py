import sys

input = sys.stdin.readline

s = input().rstrip("\n")

d = [-1] * 26

for i in range(len(s)):
    idx = ord(s[i])-97
    if d[idx] == -1:
        d[idx] = i

print(*d)