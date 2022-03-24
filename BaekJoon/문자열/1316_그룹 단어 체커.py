import sys

input = sys.stdin.readline

def check(w):
    i = 0
    visited = []
    while i < len(w):
        char = w[i]
        if char not in visited:
            visited.append(char)
            i += 1
            while i < len(w):
                if visited[-1] != w[i]:
                    break
                i += 1
        else:
            return False
    
    return True

N = int(input())
ans = 0
for _ in range(N):
    d = []
    word = input().rstrip("\n")
    if check(word):
        ans += 1
print(ans)