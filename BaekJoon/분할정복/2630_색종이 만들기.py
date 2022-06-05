import sys

input = sys.stdin.readline

N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int,input().split())))

white, blue = 0,0

def dfs(y,x,size):

    cnt = 0
    for i in range(y,y+size):
        for j in range(x,x+size):
            cnt += p[i][j]

    if cnt == 0:
        global white
        white += 1
        return

    if cnt == size * size:
        global blue
        blue += 1
        return

    new_size = size // 2
    dfs(y,x,new_size)
    dfs(y+new_size,x,new_size)
    dfs(y,x+new_size,new_size)
    dfs(y+new_size,x+new_size,new_size)

dfs(0,0,N)
print(white)
print(blue)


