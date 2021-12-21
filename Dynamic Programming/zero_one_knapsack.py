"""
문제: 무게를 쪼갤 수 없는 짐들을 가방에 넣을 때, 짐들의 가치가 최대가 되도록 해야한다.

해결방법: 다이나믹 프로그래밍으로 1. 가방에 넣을 짐의 개수 2. 가방의 무게를 고려한 모든 경우의 수를 계산한다. 
"""

cargo = [
    (4,12), # ( value, weight )
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

def zero_one_knapsack(cargo):

    capacity = 15
    pack = []

    for i in range(len(cargo)+1): # 0 ~ 5, 물품의 개수
        pack.append([])
        for c in range(capacity+1): # 0 ~ 15, 가방의 용량

            if c == 0 or i == 0: # 가방의 용량이 0 이거나, 물품의 개수가 0일때
                pack[i].append(0)
            
            elif cargo[i-1][1] <= c: # 현재 물품을 가방에 넣을 수 있을 경우
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c - cargo[i-1][1]], # 현재 물품의 가치 + 남은 용량에 담을 수 있는 물품의 최대 가치
                        pack[i-1][c] # 이전 물품의 최대 가치
                    )
                )
            else: # 물품의 무게가 가방의 무게를 초과
                pack[i].append(pack[i-1][c])
    
    return pack[-1][-1]

print(zero_one_knapsack(cargo))