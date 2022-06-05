import sys

input = sys.stdin.readline

N = int(input())
g = []
for _ in range(N):
    g.append(input().rstrip("\n"))

ans = ""
def dfs(y,x,size):
    global  ans
    cnt = 0
    for i in range(y,y+size):
        for j in range(x,x+size):
            cnt += int(g[i][j])

    if cnt == 0:
        ans += "0"
        return

    if cnt == size*size:
        ans += "1"
        return

    ans += "("
    dy,dx = [0,0,size//2,size//2], [0,size//2,0,size//2]
    for i in range(4):
        dfs(y+dy[i],x+dx[i],size//2)
    ans += ")"

dfs(0,0,N)
print(ans)