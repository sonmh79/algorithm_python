import sys
from collections import deque

"""
목표 - 팀을 반으로 나누고 -> 각 팀 점수를 계산하고 -> 최솟값 구하기

재귀 - 팀에 전체 팀원을 한명씩 추가하기
재귀 종료조건 - 팀이 반으로 나뉠 때, 각 팀의 점수를 계산한다
시간 줄이기 - 이미 점수를 계산했던 팀이면 패스, deque 쓰기 ..
"""

input = sys.stdin.readline

N = int(input())
h = N//2

s = []
for _ in range(N):
    row = list(map(int,input().split()))
    s.append(row)

visited = []
answers = []
members = set(range(N)) # 모든 팀원

def get_score(team):

    score = 0
    team = list(team)
    for i in range(len(team)-1):
        for j in range(i+1,len(team)):
            score += s[team[i]][team[j]]
            score += s[team[j]][team[i]]
    return score


def dfs(n,team):

    # 종료조건
    if len(team) == h:
        answers.append(abs(get_score(team)-get_score(members-set(team))))
        return

    for i in range(n,N):
        team.append(i)
        t1 = set(team)
        t2 = members - t1
        if t1 in visited or t2 in visited: # 시간 줄이기
            team.pop()
            continue
        dfs(i+1,team)
        team.pop() # 재귀 후 초기화

dfs(0,deque())
print(min(answers))

