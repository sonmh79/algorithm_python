import sys

"""
    풀이: 상향식으로 접근하는 동적 프로그래밍
    입력받은 배열의 인덱스를 하나씩 증가시킬때마다 해당 인덱스로부터 이전 인덱스들을 모두 탐색하면서 현재 인덱스의 값과 이전 인덱스의 값을 확인한다.
    현재 인덱스의 값보다 낮은 값을 찾으면 그 인덱스에서 최대 길이 + 1 한 값과 자신이 가진 값을 비교하며 최댓값을 선택한다.
    단, 기본 길이는 1로 설정한다.

"""

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
d = [1] * n

max_len = 1

if n == 1:
    print(1)

else:
    for i in range(1,n):
        j = i-1
        cur_n = nums[i]
        while j >=0:
            if nums[j] < cur_n:
                d[i] = max(d[i], d[j] + 1)
                max_len = max(d[i],max_len)
                
            j -= 1
    print(max_len)
