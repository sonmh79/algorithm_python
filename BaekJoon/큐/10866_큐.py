import sys
from collections import deque

input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    work = input().split()
    w = work[0]
    if w == "push_front":
        q.appendleft(work[1])
    
    elif w == "push_back":
        q.append(work[1])
    
    elif w == "pop_front":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    
    elif w == "pop_back":
        if not q:
            print(-1)
        else:
            print(q.pop())
    
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

