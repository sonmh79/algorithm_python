import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

q = deque()
for _ in range(N):
    work = input().split()
    w = work[0]
    if w == "push":
        q.append(work[1])

    elif w == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif w == "size":
        print(len(q))

    elif w == "empty":
        if not q:
            print(1)
        else:
            print(0)

    elif w == "front":
        if not q:
            print(-1)
        else:
            print(q[0])

    elif w == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
