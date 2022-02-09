import sys

"""
백트래킹, DFS
재귀 원리: 
    for문:
        가능한 연산자들 중 하나를 고른다 -> 고른 연산자로 연산 -> 나머지 연산자들로 DFS(재귀) -> 재귀 종료 후 고른 연산자를 다시 가능한 연산자들에 넣어준다

종료 조건:
    더 이상 리스트에 있는 연산자가 없다. (모든 연산 끝) -> 정답을 정답 리스트에  추가

포인트: 
    재귀 종료 후, 꺼낸 연산자를 다시 리스트에 집어 넣어 초기화 시켜주기
    재귀 종료 후, 정답도 초기화 시켜주기
"""

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

# 연산자를 모두 담아준다.
opers = [] 
opers += ["+"] * op[0]
opers += ["-"] * op[1]
opers += ["*"] * op[2]
opers += ["%"] * op[3]

# 모든 값들을 모아줄 리스트
answers = [] 

# 각 연산자에 대한 함수
def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if a < 0 and b >= 0:
        return -1 * (-1*a // b)
    elif a >= 0 and b < 0:
        return -1 * (a // b * -1) 
    return a // b

# 재귀, 백트래킹
def dfs(opers, ans, idx):
    
    # 종료 조건
    if not opers:
        answers.append(ans)
        return

    for i in range(len(opers)):
        op = opers.pop(i) # 연산자 하나를 고르기
        a = ans # 초기화를 위해 미리 정답 저장

        # 꺼낸 연산자에 따른 연산
        if op == "+":
            ans = plus(ans,numbers[idx+1])
        elif op == "-":
            ans = minus(ans,numbers[idx+1])
        elif op == "*":
            ans = mult(ans,numbers[idx+1])
        elif op == "%":
            ans = div(ans,numbers[idx+1])
        
        # 재귀 - 연산된 결과와 나머지 연산자들을 다음 재귀로 넘겨줌
        dfs(opers,ans,idx+1)

        # 재귀 종료 - 연산자 리스트와 연산된 결과 초기화 시켜주기
        opers.insert(i,op)
        ans = a

# 실행
dfs(opers,numbers[0],0)

#정답 제출
print(max(answers))
print(min(answers))

