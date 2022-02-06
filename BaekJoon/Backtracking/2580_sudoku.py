import sys

"""
    pypy3로 해서 통과 , Python3는 시간초과(83% why ?)
    1. 스토쿠에서 빈칸의 위치를 미리 구한다.
    2. 1~9까지 숫자중 가능한 숫자를 구한다.
    3. 가능한 숫자들을 하나씩 대입하며 재귀를 실행한다. (가지치기)
    4. 정답이 아닐시, 해당칸 초기화 and 후퇴 (백트래킹)
    5. 정답일시, 계속 가지치기
    6. 모든 빈칸을 채우면 종료
"""

sdk = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            blank.append((i,j))

def dfs(n):
    if n == len(blank):
        for row in sdk:
            print(*row)
        exit(0)
    
    x,y = blank[n][0], blank[n][1]

    answers = set(i for i in range(1,10))
    answers -= set(sdk[x])
    if not answers:
        return
    answers -= set([row[y] for row in sdk])
    if not answers:
        return
    r,c = x//3 * 3, y//3 * 3
    answers -= set([sdk[i][j] for i in range(r,r+3) for j in range(c,c+3)])

    for a in answers:
        sdk[x][y] = a
        dfs(n+1)
    
    sdk[x][y] = 0
        
dfs(0)
