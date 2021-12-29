import sys
from collections import defaultdict

"""
    딕셔너리에 {age:[name1,name2 ,,, name_n]} 형태로 저장한 후,
    출력 시 age에 대한 오름차순으로 출력하며 각 age가 value로 가지는 리스트를 정렬하여 출력한다.
"""

n = int(sys.stdin.readline())
d = defaultdict(list)

for _ in range(n):
    age,name = map(str,sys.stdin.readline().split())
    d[int(age)].append(name)

for age in range(1,201):
    if len(d[age]) != 0:
        names = d[age]
        for name in names:
            print(age,name)