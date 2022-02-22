import sys
from collections import defaultdict

"""
    함수 check_data: 튜플 (a,b,c)가 캐시메모리(d)에 있는지 확인 / 이미 계산된 결과가 없으면 연산 후 저장 and 리턴, 있으면 가져와서 리턴
    함수 w: 문제에서 써져있는 조건들을 모두 쓰되, 메모이제이션을 통해 하향식으로 문제를 풀어나간다. 
    만약, 입력된 결과 (a,b,c)가 이미 한 번 연산된 적이 있으면 그 값을 가져와 리턴하고, 계산한 적이 없으면 더 작은 값으로 쪼개며 탐색을 반복한다.
    
    핵심은 큰 결과값(예를 들면 (15,15,15))을 구하기 위해 더 작은 값으로 나누어 탐색하되 한 번 계산한 결과는 값을 저장해서 두 번 이상 연산하는 일이 없도록 한다.

"""


input = sys.stdin.readline

d = defaultdict(list)

def check_data(a,b,c):
    if d[(a,b,c)] != []:
        return d[(a,b,c)]
    else:
        d[(a,b,c)] = w(a,b,c)
        return d[(a,b,c)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if d[(a,b,c)] != []:
        return d[(a,b,c)]
    
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    if a < b and b < c:
        w1 = check_data(a,b,c-1)
        w2 = check_data(a, b-1, c-1)
        w3 = check_data(a, b-1, c)
        d[(a,b,c)] = w1 + w2 - w3
        return  w1 + w2 - w3

    else:
        w1 = check_data(a-1, b, c)
        w2 = check_data(a-1, b-1, c)
        w3 = check_data(a-1, b, c-1)
        w4 = check_data(a-1, b-1, c-1)
        d[(a,b,c)] = w1 + w2 + w3 - w4
        return w1 + w2 + w3 - w4

res = []
while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    r = w(a,b,c)
    res.append((a,b,c,r))

for a, b, c, r in res:
    print(f"w({a}, {b}, {c}) = {r}")


