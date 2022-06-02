import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    oper = int(input())
    if oper == 0:
        if not heap:
            print(0)

        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap,oper * -1)
