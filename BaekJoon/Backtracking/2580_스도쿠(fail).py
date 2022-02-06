import sys

sdk = []
for _ in range(9):
    sdk.append(list(map(int,sys.stdin.readline().split())))

def check_answers(i,j):
    """ i행 j열에 들어갈 수 있는 모든 수 리턴 """
    ans = []

    row = sdk[i]
    column = [row[j] for row in sdk]
    box_row = i//3 * 3
    box_col = j//3 * 3
    box = [sdk[r][c] for r in range(box_row,box_row+3) for c in range(box_col,box_col+3)]

    for i in range(1,10):
        if i not in row and i not in column and i not in box:
            ans.append(i)
    
    return ans

def is_finish():
    for i in range(9):
        for j in range(9):
            if sdk[i][j] == 0:
                return False
    return True

def dfs(i,j):
    answers = check_answers(i,j)

    if not answers: # 종료 조건 - 해당 칸에서 가능한 숫자가 없으면 후퇴 (백트래킹)
        return

    for a in answers:
        sdk[i][j] = a

        r,c = i,j # r,c 는 다음 빈칸의 행,열 인덱스
        while r < 9 and c < 9: # 빈칸을 찾아 이동
            
            if sdk[r][c] == 0:
                dfs(r,c) # 빈칸 발견하면 재귀
                break

            if c == 8:
                r += 1
                c = 0
            else:
                c += 1
        
        if is_finish(): # 빈칸이 없으면 후퇴 => 다음 정답을 고려할 필요가 없기 때문
            return
    
    sdk[i][j] = 0 # 빈칸 초기화 => 후퇴를 했다는 것은 현재칸의 숫자도 정답이 아니기 때문

for i in range(9):
    for j in range(9):
        if sdk[i][j] == 0:
            dfs(i,j)
            break
        break

for row in sdk:
    print(*row)

