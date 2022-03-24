import sys

input = sys.stdin.readline

N = int(input())

stack = []
def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if not stack:
        return 1

    return 0

def top():
    if not stack:
        return -1

    return stack[-1]

answer = []
for _ in range(N):
    work = input().split()
    w = work[0]
    if w == "push":
        push(work[1])
    elif w == "pop":
        answer.append((pop()))
    elif w == "size":
        answer.append(size())
    elif w == "empty":
        answer.append(empty())
    elif w == "top":
        answer.append(top())

for a in answer:
    print(a)