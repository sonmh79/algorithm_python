import sys

input = sys.stdin.readline

n, capacity = map(int, input().split())
pack = [[0 for _ in range(capacity+1)]] 

for i in range(1,n+1):
    w,v = map(int,input().split())
    pack.append([])
    for c in range(capacity+1):
        if c == 0:
            pack[i].append(0)
        elif w <= c:
            pack[i].append(
                max(pack[i-1][c],pack[i-1][c-w]+v)
            )
        else:
            pack[i].append(pack[i-1][c])

print(pack[-1][-1])

"""
    풀이: 2차원 표를 통해 모든 경우의 수를 구하자
    이 문제는 가방의 용량을 고려해 주어진 물품 중 가장 큰 가치를 만드는 물품의 조합을 구해야 한다.
    따라서, 가방의 용량을 열로, 물품의 수를 행으로 하는 2차원 테이블을 만들어 모든 경우의 수를 구해 보자.
    이래서 상향식 풀이 방법을 Tabulation이라고 칭하는 건가보다 하고 새삼 느낀다.

"""