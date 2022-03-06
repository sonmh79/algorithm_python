import sys

"""
    풀이: 
    바이토닉 수열은 '증가하는 수열 + 최댓값 + 감소하는 수열' 로 이루어져있다.
    증가하는 부분의 수열의 길이를 먼저 구해 저장한다.
    수열의 이전 인덱스의 값이 현재 인덱스의 값보다 크면 감소하는 수열로 판단한다.
"""


input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
inc = [1] * n # 증가하는 부분 수열의 길이 저장
bi = [1] * n # 바이토닉 부분 수열의 길이 저장


for i in range(1,n):
    j = i-1
    cur_n = nums[i]
    while j >=0:
        if nums[j] < cur_n:
            inc[i] = max(inc[i], inc[j] + 1)
        if nums[j] > cur_n:
            bi[i] = max(bi[i], bi[j] + 1)   
        bi[i] = max(bi[i], inc[i])
        j -= 1
print(max(bi))

