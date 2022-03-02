import sys

"""
    풀이: 백준 문제 2579번 계단 오르기와 비슷하지만 다른 문제이다.

    조건 1. 포도주를 마시고 빈 잔은 그대로 놓는다.
    조건 2. 포도주를 세 잔 연속으로 마실 수 없다.

    조건에 포도주를 반드시 마셔야 하는 잔의 간격이 정해져 있지 않다.
    따라서, 1부터 n잔까지 최대 마실 수 있는 포도주의 양을 저장해 놓는다.
    여기에 더해 조건 2만 고려하여 점화식을 세운다.
    1. i-3번쨰 잔까지 최대 마실 수 있는 포도주 양 + i-1, i번째 포도주를 마시는 경우
    2. i-2번째 잔까지 최대 마실 수 있는 포도주 양 + + i번째 포도주를 마시는 경우
    둘 중, 최대값을 구해 저장한다.
"""

input = sys.stdin.readline

n = int(input())
drinks = [0] * (n+1)
max_drinks = [0] * (n+1)

for i in range(n):
    drinks[i+1] = int(input())

if n <= 2:
    print(sum(drinks))

else:
    ans = 0
    max_drinks[1] = drinks[1]
    max_drinks[2] = max(ans, drinks[1] + drinks[2])
    ans = max_drinks[2]
    for i in range(3,n+1):
        max_drinks[i] = max(max_drinks[i-3] + drinks[i-1] + drinks[i], max_drinks[i-2] + drinks[i], ans)
        ans = max_drinks[i]
    print(ans)