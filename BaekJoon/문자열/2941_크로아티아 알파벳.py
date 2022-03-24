import sys

input = sys.stdin.readline

s = input().rstrip("\n")

d = {
    "c":["c=","c-"],
    "d":["dz=","d-"],
    "l":["lj"],
    "n":["nj"],
    "s":["s="],
    "z":["z="]
    }

ans = 0
i = 0
while i < len(s):
    char = s[i]
    flag = True
    if char in d:
        for word in d[char]:
            if s[i:i+len(word)] == word:
                ans += 1
                i += len(word)-1
                flag = False
                break
        i += 1
        if flag:
            ans += 1
    else:
        ans += 1
        i += 1
print(ans)