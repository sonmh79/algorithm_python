from collections import deque
import sys

input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    p = input().rstrip("\n")
    n = int(input())
    X = input().split(",")
    X[0] = X[0].lstrip("[")
    X[-1] = X[-1].rstrip("]\n")
    xs = deque()
    for x in X:
        if x.isdigit():
            xs.append(int(x))
    
    def sol(front):
        for func in p:
            if func == "R":
                if front:
                    front = False
                else:
                    front = True
            else:
                if not xs:
                    return -1
                
                if front:
                    xs.popleft()
                else:
                    xs.pop()
        
        if front:
            return xs
        else:
            return list(xs)[::-1]

    answer.append(sol(True))
for a in answer:
    if a == -1:
        print("error")
    else:
        s = "["
        for i,n in enumerate(a):
            char = str(n)
            s += char
            s += ","
        s = s.rstrip(",")
        s += "]"
        print(s)

"""
    함정: 함수의 연산을 모두 수행한 뒤의 배열의 결과가 빈 리스트일 수 있다.
"""