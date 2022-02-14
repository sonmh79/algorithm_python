import sys

"""
pypy3로 시간초과 해결 ㅠㅠ

풀이: 각 행의 열들을 탐색 -> 이전에 놓여진 퀸의 열과 대각선에 해당되는지 확인한다.
재귀 종료 조건: 총 N개의 퀸이 놓여져 있으면 재귀 종료


"""

input = sys.stdin.readline

N = int(input())
columns = [False for _ in range(N)]
queen = []

a = 0 # 정답, 모든 가능한 경우의 수

def is_possible(r,c):
    for row, col in queen:
        if abs(row-r) == abs(col-c): # 대각선 방향 확인
            return False
    return True

def dfs(r):

    if len(queen) == N:
        global a
        a+=1
        return
    
    for c in range(N):
        if columns[c] == True: # 이전 퀸들이 놓여져 있는 열인지 확인한다.
            continue
        if is_possible(r,c): # 현재 위치에서 대각선에 이전 퀸들이 없을 때
            queen.append((r,c))
            columns[c] = True
            dfs(r+1)
            queen.pop()
            columns[c] = False
    return
        
dfs(0)
print(a)

