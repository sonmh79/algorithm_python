import sys
from collections import defaultdict

"""
    딕셔너리에 {y:[x1,x2 ,,, xn]} 형태로 저장한 후,
    출력 시 y에 대한 오름차순으로 출력하며 각 y가 value로 가지는 리스트를 정렬하여 출력한다.
"""

n = int(sys.stdin.readline())
d = defaultdict(list)

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    d[y].append(x)

for y in range(-100000,100001):
    if len(d[y]) != 0:
        xs = d[y]
        xs.sort()
        for x in xs:
            print(x,y)