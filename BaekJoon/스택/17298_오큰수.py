import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

stack = [(0,nums[0])]
answer = [-1] * N

for i in range(1,len(nums)):
    cur_num = nums[i]
    pre_idx, pre_num = stack[-1]
    if pre_num < cur_num:
        while stack:
            j,n = stack.pop()
            if n < cur_num:
                answer[j] = cur_num
            else:
                stack.append((j,n))
                break
    stack.append((i,cur_num))
print(*answer)
    
"""
    스택에 (인덱스, 값)을 원소로 넣어 각 값마다 비교한다.
    스택에 있는 값들은 오큰수를 찾지 못한 위치와, 인덱스 들이다.
    스택의 마지막 값과 현재 값을 비교하여 오큰수를 찾으면 스택에 있는 수들을 꺼내 정답의 해당 위치에 오큰수를 입력해준다.
"""