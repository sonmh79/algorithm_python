import sys

"""
    풀이: 문제를 해석하면 피보나치의 원리에 따라 값을 구해야 함을 알 수 있다.
    단, 주어지는 n의 값이 최대 1,000,000 이기 때문에 15746으로 나누지 않으면 메모리 초과 + 시간초과가 난다.
    c = a + b 이며, c % x 의 나머지 = (a % x 의 나머지 + b % x 의 나머지) % x 의 나머지이다. (이때, x = 15746)
"""

input = sys.stdin.readline

n = int(input())
m = 15746
d = [0] * 3
d[1] = 1
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    d[2] = 2
    for i in range(3,n+1):
        n1, n2, n3 = d[0]%m, d[1]%m, d[2]%m
        d[-1] = (n2+n3)%m
        d[-2] = n3
    print(d[-1])