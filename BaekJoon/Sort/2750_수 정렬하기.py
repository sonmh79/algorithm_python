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

for num in l:
    print(num)