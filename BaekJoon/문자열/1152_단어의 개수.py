import sys

input = sys.stdin.readline

s = input().rstrip("\n").split(" ")

cnt = 0

for word in s:
    if word == "":
        pass
    else:
        cnt += 1

print(cnt)