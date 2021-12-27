import sys

""" 
    풀이 - 재귀 
    문제 정의 - 하노이 탑을 3번째 장대로 옮기되, 1. 한 번의 한 개의 원판만 옮길 수 있다. 2. 원판은 항상 위의 것이 아래 것보다 작아야 한다.
    원리 - n-1개의 원판을 보조 장대에 옮긴다 -> n번째 원판을 목표 장대(3번째)로 옯긴다. -> 보조 장대의 n-1개의 원판을 목표 장대로 옮긴다.
    종료 조건 - 정의 1번에 따라 n==1일 때, 원판을 옮기고 재귀 종료, 백트래킹 시작
"""

n = int(sys.stdin.readline())

ans = []

def hanoi(n,start,end,sub):

    if n == 1:
        ans.append((start,end))
        return
    
    hanoi(n-1,start,sub,end)
    ans.append((start,end))
    hanoi(n-1,sub,end,start)

hanoi(n,1,3,2)
print(len(ans))
for s,e in ans:
    print(s,e)