from copy import deepcopy
def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:x[1])
    t = deepcopy(tickets)
    q = [(["ICN"],t)]
    while q:
        route,left_tickets = q.pop(0)
        node = route[-1]
        if len(route) == len(tickets)+1:
            return route
        for i in range(len(left_tickets)):
            dep,arv = left_tickets[i]
            if node == dep:
                left_tickets.remove([dep,arv])
                t = deepcopy(left_tickets)
                q.append((route+[arv],t))
                left_tickets.insert(i,[dep,arv])
    return answer

"""
dfs, 가능한 모든 경로를 큐에 포함시켜서 확인하기
남은 티켓들을 deepcopy를 써서 서로 다른 리스트로 관리해준다.
"""