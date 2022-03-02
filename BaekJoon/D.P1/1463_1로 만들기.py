import sys

"""
    풀이: 상향식 풀이로 구하고자하는 타겟(n)에 접근한다.

    n의 최소 연산 수는 다음의 세 가지 경우 중 최솟값이다.
    1. n-1의 최소 연산 수 + 1
    2. n//2의 최소 연산 수 + 1 (단, n은 2의 배수)
    3. n//3의 최소 연산 수 + 1(단, n은 3의 배수)

    1부터 n까지 순서대로 위의 세 가지 경우를 검토하며 값을 구한다.

    1은 0번의 연산이 필요하다.
    2는 1번의 연산이 필요하다.(2 나누기 1 or 2 빼기 1)
    3은 1번의 연산이 필요하다.(3 나누기 1)
    ...

"""

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