import sys

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

# 1. 팀 소트
# l.sort()

# 2. 버블 정렬 O(n^2)
# n = len(l)
# for i in range(n-1,0,-1):
#     for j in range(i):
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]

# 3. 퀵 소트 O(nlogn) ~ O(n^2)
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     pivot = len(array) // 2

#     less, equal, more = [], [], []

#     p = array[pivot]
#     for i in range(len(array)):
#         if array[i] > p:
#             more.append(array[i])
#         elif array[i] == p:
#             equal.append(array[i])
#         else:
#             less.append(array[i])
    
#     return quick_sort(less) + equal + quick_sort(more)

# l = quick_sort(l)

for num in l:
    print(num)