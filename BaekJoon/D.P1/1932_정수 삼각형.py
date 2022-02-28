import sys

"""
    풀이: 
    정수 삼각형의 한 줄씩 리스트로 저장한다. 
    현재 줄의 0번째 값은 반드시 이전 줄의 0번째 값을 더하고, 현재 줄의 마지막 값은 이전 줄의 마지막 값을 더한다. 
    그 외, 현재 줄의 i번째 값은 이전 줄의 i-1과 i번째 값 중 최댓값을 더한다.
    현재 줄을 다시 저장한다.
    최종적으로 저장된 리스트의 최댓값을 출력한다.
"""

input = sys.stdin.readline

n = int(input())
answer = list(map(int,input().split()))
for _ in range(n-1):
    cur_line = list(map(int,input().split()))
    for i in range(len(cur_line)):
        if i == 0:
            cur_line[i] += answer[0]
        elif i == len(cur_line)-1:
            cur_line[i] += answer[-1]
        else:
            cur_line[i] += max(answer[i-1],answer[i])
    answer = cur_line
print(max(answer))