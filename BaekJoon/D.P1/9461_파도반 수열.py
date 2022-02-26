import sys

"""
    풀이: 타뷸레이션(상향식) 방식
    점화식 P(N) = P(N-1) + P(N-5)를 찾아낸다면 동적계획법으로 쉽게 풀이가 가능하다.
    다만, 여러 N 중 가장 큰 수를 저장하고 한 번만 계산을 수행함으로써 다른 N들을 바로 출력할 수 있도록 풀이했다.
"""


input = sys.stdin.readline

T = int(input())
d = [0]*101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2
max_n = -sys.maxsize
list_n = []
for _ in range(T):
    n = int(input())
    list_n.append(n)
    max_n = max(n,max_n)

for i in range(6,max_n+1):
        d[i] = d[i-1]+d[i-5]

for n in list_n:
    print(d[n])