import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

nums.sort()
ans = 0

for i,num in enumerate(nums):
    ans += num * (n-i)
print(ans)

"""
풀이: 1. 오름차순으로 정렬
2. 사람들이 순서대로 atm기를 이용한다.
3. 뒤 사람들은 앞 사람들의 이용 시간을 기다려야 한다.
"""