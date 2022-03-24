import sys

input = sys.stdin.readline

s = []
N=int(input())
for _ in range(N):
    s.append(int(input()))

p = 0
stack = []
answer = []
for i in range(1,N+1):

    if i == s[p]:
        stack.append(i)
        answer.append("+")
        while stack:
            if s[p] == stack[-1]:
                p += 1
                stack.pop()
                answer.append("-")
            else:
                break
    else:
        stack.append(i)
        answer.append("+")

while stack:
    if stack.pop() != s[p]:
        answer.append("NO")
        break
    else:
        answer.append("-")
        
if answer[-1] == "NO":
    print("NO")
else:
    for ans in answer:
        print(ans)