import sys

n,m = map(int, sys.stdin.readline().split())

"""
    백트래킹(Backtracking, 퇴각검색)
    DFS를 통해 모든 규칙을 검사하되, 규칙을 만족시키지 못하면 퇴각하여 이전 분기점에서 다시 탐색한다.
    완전탐색하는 브루트포스(Brute force)와 달리 조건을 설정하여 탐색 효율을 높일 수 있다.

    목표: 중복되는 수열 여러 번 출력 x ( 중복을 포함하는 조합 ? )
"""


lst = []
def dfs():

    if len(lst) == m:

        print(*[n for n in lst])
        return

    for i in range(1,n+1):
        if (lst and i >= lst[-1]) or not lst:
            lst.append(i)
            dfs()
            lst.pop()
dfs()