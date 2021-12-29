import sys
from collections import defaultdict

"""
    딕셔너리에 {x:[y1,y2 ,,, yn]} 형태로 저장한 후,
    출력 시 x에 대한 오름차순으로 출력하며 각 x가 value로 가지는 리스트를 정렬하여 출력한다.
"""

n = int(sys.stdin.readline())
d = defaultdict(list)

for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    d[x].append(y)

for x in range(-100000,100001):
    if len(d[x]) != 0:
        ys = d[x]
        ys.sort()
        for y in ys:
            print(x,y)