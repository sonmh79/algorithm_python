import sys

"""
    풀이: 각 집을 r,g,b로 칠할 수 있는 모든 경우를 구한다.
    1. r로 칠할 경우, 다음 집은 g,b 중 최소 비용을 가진 색깔을 칠한다.
    2. g로 칠할 경우, 다음 집은 r,b 중 최소 비용을 가진 색깔을 칠한다.
    3. b로 칠할 경우, 다음 집은 r,g 중 최소 비용을 가진 색깔을 칠한다.
    위 세가지 경우 중 최소 비용을 구해 출력한다.
"""

input = sys.stdin.readline

n = int(input())
cost = []
r,g,b = map(int,input().split())
cost.append([r,g,b])
for i in range(1,n):
    r,g,b = map(int,input().split())
    pR,pG,pB = cost[-1]
    r = r + min(pB,pG)
    g = g + min(pR,pB)
    b = b + min(pR,pG)
    cost.append([r,g,b])
print(min(cost[-1]))