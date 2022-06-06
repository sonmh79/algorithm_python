import sys

input = sys.stdin.readline

A,B,C = map(int,input().split())

def recursive(A,B,C):
    if B == 1:
        return A % C

    if B%2:
        return (A * recursive(A, B // 2, C)**2) % C
    else:
        return (recursive(A,B//2,C)**2)%C

print(recursive(A, B, C))
