import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))
cost = list(map(int,input().split()))

cur_cost = cost[0]
ans = 0

for i in range(1,len(cost)):
    if cur_cost < cost[i]:
        ans += d[i-1] * cur_cost
    else:
        ans += d[i-1] * cur_cost
        cur_cost = cost[i]
print(ans)

"""
풀이: 현재 주유소의 가격과 다음 주유소의 가격을 비교한다.
현재 주유소의 가격이 더 싸다면, 현재 주유소의 가격으로 주유한다.
다음 주유소의 가격이 더 싸다면, 다음 주유소까지만 주유하고 다음 주유소 가격으로 주유한다.
"""