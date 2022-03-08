import sys

input = sys.stdin.readline

s1 = input().rstrip("\n")
s2 = input().rstrip("\n")

d = [0]*len(s2)

for i,char in enumerate(s2):
    j = i
    end = len(s1)
    cnt = 0
    while j >= 0:
        search = s1[:end]
        for k in range(end-1,-1,-1):
            if search[k] == s2[j]:
                end = k
                cnt += 1
                break
        j-=1
    d[i] = cnt
print(d)


