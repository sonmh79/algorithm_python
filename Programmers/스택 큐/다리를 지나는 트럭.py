from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque()
    sec = 0
    while truck_weights:
        for i in range(len(bridge)):
            bridge[i][0] -= 1
        
        if bridge and bridge[0][0] == 0:
            _,tw = bridge.popleft()
            weight += tw

        if len(bridge) < bridge_length and truck_weights[0] <= weight:
            w = truck_weights.popleft()
            weight -= w
            bridge.append([bridge_length,w])

        sec += 1
    
    while bridge:
        for i in range(len(bridge)):
            bridge[i][0] -= 1
        
        if bridge and bridge[0][0] == 0:
            _,tw = bridge.popleft()
            weight += tw
        sec += 1
    return sec

"""
    큐에 [남은 시간, 무게] 를 넣어 관리한다. 시간의 흐름을 고려해 큐에 있는 남은 시간을 1씩 감소시키고 남은 시간이 0일 때 큐에서 제거한다. 
"""