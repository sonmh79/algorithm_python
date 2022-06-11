import sys

N = int(input())
INF = int(3e10)
matrix = [[0,0]]
for _ in range(N):
    matrix.append(list(map(int,input().split())))
dp = [[INF for _ in range(N+1)] for _ in range(N+1)]

def mm(l,r):

    if l == r:
        return 0

    if l == r+1:
        return matrix[l][0] * matrix[r][0] * matrix[r][1]

    if dp[l][r] == INF:
        for i in range(l,r):
            dp[l][r] = min(dp[l][r], mm(l,i) + mm(i+1,r) + matrix[l][0] * matrix[i][1] * matrix[r][1])
    return dp[l][r]
mm(1,N)
print(dp[1][N])
