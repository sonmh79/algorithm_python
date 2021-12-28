import sys

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

# 1. 팀 소트
# l.sort()

# 2. 병합 정렬 O(nlogn) -> 시간 초과 ,,
# def merge_sort(array):

#     if len(array) <= 1:
#         return array
    
#     mid = len(array) // 2

#     a1 = merge_sort(array[:mid])
#     a2 = merge_sort(array[mid:])

#     result = []
#     while a1 and a2:
#         if a1[0] > a2[0]:
#             result.append(a2.pop(0))
#         else:
#             result.append(a1.pop(0))
    
#     if a1:
#         result += a1
#     if a2:
#         result += a2
    
#     return result

# l = merge_sort(l)

for num in l:
    print(num)