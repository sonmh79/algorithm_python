from collections import deque

def solution(priorities, location):
    
    dq = deque()
    pq = []
    for i,p in enumerate(priorities):
        dq.append((i,p))
    
    pq.append(dq.popleft())
    while dq:
        if not pq or pq[-1][1] >= dq[0][1]:
            pq.append(dq.popleft())
        else:
            stack = []
            while pq:
                if pq[-1][1] < dq[0][1]:
                    stack.append(pq.pop())
                else:
                    break
            dq += stack[::-1]
    
            
    print(pq)
    for i in range(len(pq)):
        if pq[i][0] == location:
            return i+1
            
        