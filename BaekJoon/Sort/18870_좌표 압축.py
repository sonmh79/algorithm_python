import sys

"""
    딕셔너리 key: 주어진 x좌표, value: 정렬된 x 좌표 리스트에서 인덱스 값
    정렬된 리스트에서 x의 인덱스의 의미는 몇 번째로 작은 수임을 의미한다.
"""

n = int(sys.stdin.readline())
list_x = list(map(int, sys.stdin.readline().split()))

sorted_x = sorted(list(set(list_x)))

answer = {}
for i in range(len(sorted_x)):
    answer[sorted_x[i]] = i

for a in list_x:
    print(answer[a], end=" ")
