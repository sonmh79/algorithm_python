import sys

input = sys.stdin.readline

N,M = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

B = []
M,K = map(int,input().split())
for _ in range(M):
    B.append(list(map(int,input().split())))

ans = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for m in range(M):
            ans[i][j] += A[i][m]*B[m][j]
for a in ans:
    print(*a)
