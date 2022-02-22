import sys

"""
    풀이: 주어지는 숫자 n마다 0이 출력되는 횟수와 1이 출력되는 횟수를 저장한다.
    0: (1,0)
    1: (0,1)
    2: 1이 가진 값 + 0이 가진 값 => (1,1)
    ...
    n: n-1이 가진 값 + n-2가 가진 값
    작은 값들의 값을 연산 후 저장하고 사용하며 큰 값의 문제를 풀어내는 방식(타뷸레이션)
"""


input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    d = [(0,0)] * (n+1)
    d[0] = (1,0)
    if n == 0:
        print(*d[0])
    elif n == 1:
        d[1] = (0,1)
        print(*d[1])
    else:
        d[1] = (0,1)
        for i in range(2,n+1):
            d[i] = (d[i-1][0] + d[i-2][0],d[i-1][1] + d[i-2][1])
        print(*d[n])