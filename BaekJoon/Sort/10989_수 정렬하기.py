import sys

""" 배열 또는 딕셔너리를 활용한 메모리 관리, 정렬 """

n = int(sys.stdin.readline())

d = [0]  * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    d[num] += 1

for i in range(1,10001):
    if d[i] != 0:
        for _ in range(d[i]):
            print(i)