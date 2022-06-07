import sys

input = sys.stdin.readline

N,B = map(int,input().split())
M = []
for _ in range(N):
    M.append(list(map(lambda x: int(x) % 1000, input().split())))

def mult(m1,m2):

    new_m = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                new_m[i][j] += m1[i][k] * m2[k][j]
        new_m[i] = list(map(lambda x:x%1000,new_m[i]))
    return new_m

def dac(m,b):

    if b == 1:
        return m

    mat = dac(m,b//2)
    if b%2:
        return mult(m,mult(mat,mat))
    else:
        return mult(mat,mat)

for row in dac(M,B):
    print(*row)