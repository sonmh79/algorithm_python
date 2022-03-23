import sys

input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    R, S = input().split()
    ans = ""
    for i in range(len(S)):
        for _ in range(int(R)):
            ans += S[i]
    answer.append(ans)

for a in answer:
    print(a)