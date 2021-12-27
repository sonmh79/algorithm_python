import sys

n = int(sys.stdin.readline())
p = []
for _ in range(n):
    w,h = map(int,sys.stdin.readline().split())
    p.append((w,h))

rank = []
for w1,h1 in p:
    cnt = 1
    for w2, h2 in p:
        if w1 == w2 and  h1 == h2:
            continue
        if w1 < w2 and h1 < h2:
            cnt += 1
    rank.append(cnt)

for r in rank:
    print(r, end=" ")