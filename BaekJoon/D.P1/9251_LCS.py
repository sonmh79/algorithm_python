import sys

input = sys.stdin.readline

s1 = "0" + input().rstrip("\n")
s2 = "0" + input().rstrip("\n")

d = [[0]*len(s1)]

for i in range(1,len(s2)):
    d.append([0]*len(s1))
    for j in range(1,len(s1)):
        if s2[i] == s1[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1],d[i-1][j])

print(d[-1][-1])

"""
풀이: 테이블 만들기
    0 A C A Y K P
[
0   [0, 0, 0, 0, 0, 0, 0],
C   [0, 0, 1, 1, 1, 1, 1],
A   [0, 1, 1, 2, 2, 2, 2],
P   [0, 1, 1, 2, 2, 2, 3],
C   [0, 1, 2, 2, 2, 2, 3],
A   [0, 1, 2, 3, 3, 3, 3],
K   [0, 1, 2, 3, 3, 4, 4]]
"""