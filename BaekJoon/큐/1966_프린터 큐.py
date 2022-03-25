from collections import deque
import sys

input = sys.stdin.readline
answer = []
for _ in range(int(input())):
    N,target = map(int,input().split())
    pq = deque()
    for i,p in enumerate(list(map(int,input().split()))):
        pq.append((i,p))
    
    q = [pq.popleft()]
    while pq:
        idx,p = pq.popleft()
        stack = []
        while q:
            if q[-1][1] < p:
                stack.append(q.pop())
            else:
                break
        q.append((idx,p))
        pq += stack[::-1]
    for i in range(1,N+1):
        idx,_ = q[i-1]
        if idx == target:
            answer.append(i)
            break
for a in answer:
    print(a)

"""
    목표: 원하는 순서의 문서를 몇번째로 출력하는지 궁금함
    주어진 큐를 하나씩 꺼내 (인덱스, 우선순위)로 만들어 우선순위 큐에 넣는다.
    우선순위 큐를 하나씩 꺼내며 출력 큐에 집어 넣는다.
        단, 출력 큐에 자신보다 낮은 우선순위가 있으면 모두 자신 뒤로 보내야한다.
"""