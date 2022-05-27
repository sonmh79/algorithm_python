import sys

input = sys.stdin.readline

N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

for i in range(1, N + 1):
    if i + T[i] - 1 <= N:
        dp[i] = max(dp[i], P[i])
        for j in range(i + T[i], N + 1):
            if j + T[j] - 1 <= N:
                dp[j] = max(dp[j], dp[i] + P[j])
        dp[i] = max(dp[i], dp[i - 1])
    else:
        dp[i] = dp[i - 1]

print(dp[-1])
