import sys

""" 완전탐색 배운점: 완전 탐색인 문제는 전부 탐색 후 정답을 리턴하자 .. """

n, target = map(int,sys.stdin.readline().split())

cards = list(map(int,sys.stdin.readline().split()))

def blackJack(cards):
    ans = 0
    for i in range(0,len(cards)-2):
        
        for j in range(i+1,len(cards)-1):
            
            for k in range(j+1,len(cards)):
                sum = cards[i] + cards[j] + cards[k]
                if sum <= target:
                    if ans < sum:
                        ans = sum
    return ans
print(blackJack(cards))

    