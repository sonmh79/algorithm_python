import sys

n = int(sys.stdin.readline())

d = [0] * (n+1)
d[1] = 0
if n == 1:
    print(0)
else:
    for i in range(2,n+1):
        subs = []
        if i%2 == 0:
            subs.append(d[i//2]+1)
        if i%3 == 0:
            subs.append(d[i//3]+1)
        subs.append(d[i-1]+1)

        d[i] = min(subs)

    print(d[n])