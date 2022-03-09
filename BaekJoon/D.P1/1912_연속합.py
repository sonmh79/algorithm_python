import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))
for i in range(1,n):
    if nums[i] + nums[i-1] >= 0:
        nums[i] = max(nums[i] + nums[i-1],nums[i])
print(max(nums))

"""
    풀이: 연속합을 구하기 위해 이전의 값들을 더해본다.
    더한 값이 마이너스라면 더 이상 더하지 않고 원래 값을 유지한다.
    더한 값이 양수라면, 더한 값과 원래 값 중 큰 값을 선택한다.
    최종적으로 리스트의 최댓값을 출력한다.
"""