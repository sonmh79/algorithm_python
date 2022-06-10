import sys

T = int(input())
for _ in range(T):
    K = int(input())
    cost = [0] + list(map(int,input().split()))
    pre_sum = [0 for _ in range(K+1)]
    for i in range(1,K+1):
        pre_sum[i] = pre_sum[i-1]+cost[i]

    d = [[float('inf') for _ in range(K+1)] for _ in range(K+1)]

    for j in range(1,K+1):
        for i in range(j+1,0,-1):
            if i == j:
                d[i][j] = 0
            for k in range(j-1,i-1,-1):
                d[i][j] = min(d[i][j], d[i][k] + d[k+1][j] + pre_sum[j]-pre_sum[i-1])
    print(d[1][K])