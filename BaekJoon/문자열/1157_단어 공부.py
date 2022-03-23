import sys
from collections import defaultdict

input = sys.stdin.readline
s = input().rstrip("\n")
d = defaultdict(int)

t = 0
for i in range(len(s)):
    char = s[i]
    idx = ord(char)
    if 97 <= idx < 123:
        idx -= 32
        char = chr(idx)
    d[char] += 1
    t = max(t,d[char])

answer = []
for k in d:
    if d[k] == t:
        answer.append(k)

if len(answer) >= 2:
    print("?")
else:
    print(*answer)