import sys

input = sys.stdin.readline

n = int(input())
d = [1] * (n)
lines = []
for _ in range(n):
    a,b = map(int,input().split())
    lines.append((a,b))

lines.sort()

for i in range(n-1):
    _,y1 = lines[i]
    for j in range(i+1,n):
        _,y2 = lines[j]
        if y1 < y2:
            d[j] = max(d[i]+1,d[j])

print(n - max(d))

"""
Longest Increasing Subsequence 문제

전깃줄의 출발지를 기준으로 오름차순으로 정렬한다.
도착지 기준 LIS를 구한다.
전체 n 에서 빼준다.

"""