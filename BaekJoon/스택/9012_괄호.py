import sys

input = sys.stdin.readline

answer = []
def VPS(s,stack):
    for p in s:
        if p == "(":
            stack.append(0)
        
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    if not stack:
        return True
    else:
        return False

for _ in range(int(input())):
    s = input().rstrip("\n")
    if VPS(s,[]):
        answer.append("YES")
    else:
        answer.append("NO")
        
for a in answer:
    print(a)