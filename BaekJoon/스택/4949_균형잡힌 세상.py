import sys

input = sys.stdin.readline

answer = []
def check(seq,stack):
    for char in seq:
        if char == "(":
            stack.append(0)
        elif char == "[":
            stack.append(1)
        elif char == ")":
            if not stack:
                return False
            
            if stack.pop() != 0:
                return False

        elif char == "]":
            if not stack:
                return False
            
            if stack.pop() != 1:
                return False
    
    if not stack:
        return True
    else: 
        return False

while True:
    seq = input().rstrip("\n")
    if seq == ".":
        for ans in answer:
            print(ans)
        break
    if check(seq,[]):
        answer.append("yes")
    else:
        answer.append("no")
    