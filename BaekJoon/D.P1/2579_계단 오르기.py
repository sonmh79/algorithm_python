import sys

"""
    풀이:
    조건1 - 1계단 혹은 2계단씩 이동 가능
    조건2 - 세 계단 연속 이동 불가
    조건3 - 마지막 계단으로 이동해야 함

    n번째 계단에서 점수의 최댓값은 1. n-2번째 계단에서 2계단 점프한 경우, 2. n-1번째 계단에서 1계단 이동한 경우 중 최댓값이다.
    2번의 경우는 조건 2를 고려해 n-3번째 계단에서 출발해야 한다는 전제 조건이 필요하다.
    따라서, 이를 점화식으로 표현하면 f[n] = cost[i] + max(f[n-2], f[n-3]+cost[n-1])
"""

input = sys.stdin.readline

n = int(input())
f = [0] * (n+1)
cost = [0] * (n+1)
for i in range(n):
    cost[i+1] = int(input())

if n <= 2:
    print(sum(cost))
else:
    f[1] = cost[1]
    f[2] = cost[1] + cost[2]
    for i in range(3,n+1):
        f[i] = cost[i] + max(f[i-2],f[i-3]+cost[i-1])
    print(f[n])


