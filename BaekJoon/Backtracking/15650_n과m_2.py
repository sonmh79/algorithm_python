import sys

n,m = map(int, sys.stdin.readline().split())

"""
    백트래킹(Backtracking, 퇴각검색)
    DFS를 통해 모든 규칙을 검사하되, 규칙을 만족시키지 못하면 퇴각하여 이전 분기점에서 다시 탐색한다.
    완전탐색하는 브루트포스(Brute force)와 달리 조건을 설정하여 탐색 효율을 높일 수 있다.

    목표: 백트래킹을 하되 오름차순 조건을 만족해야한다.
"""

lst = []
def dfs():

    if len(lst) == m:

        print(*[n for n in lst])
        return

    for i in range(1,n+1):
        if i not in lst: # 리스트가 비어있으면 바로 추가
            if len(lst) == 0:
                lst.append(i)
                dfs()
                lst.pop()
            else: # 리스트가 비어있지 않으면 오름차순인지 확인하고 추가
                if i > lst[-1]:
                    lst.append(i)
                    dfs()
                    lst.pop()
            
dfs()