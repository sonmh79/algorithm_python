import sys
import heapq

input = sys.stdin.readline

N = int(input())

l_heap = [] # max heap, 루트에 중간값
r_heap = [] # min heap

for i in range(1,N+1):
    n = int(input())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap,(-n,n))
    else:
        heapq.heappush(r_heap,(n,n))

    if l_heap and r_heap and l_heap[0][1] > r_heap[0][1]:
        lk, lv = heapq.heappop(l_heap)
        rk, rv = heapq.heappop(r_heap)
        heapq.heappush(r_heap,(-1 * lk, lv))
        heapq.heappush(l_heap,(-1 * rk, rv))

    if i % 2 == 1:
        print(l_heap[0][1])
    else:
        print(min(l_heap[0][1],r_heap[0][1]))



