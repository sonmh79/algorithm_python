import sys
from collections import deque

input = sys.stdin.readline

flag = True
q = deque(range(1,int(input())+1))

while q:

    card = q.popleft()

    if flag:
        flag = False
    else:
        flag = True
        q.append(card)

print(card)
