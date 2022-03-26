from collections import deque

def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses)
    for i in range(len(progresses)):
        rest_p = 100 - progresses[i]
        q,r = divmod(rest_p,speeds[i])
        if r == 0:
            days[i] = q
        else:
            days[i] = q + 1
    
    days = deque(days)
    while days:
        d = [days.popleft()]
        while days and d[0] >= days[0]:
            d.append(days.popleft())
        answer.append(len(d))
    return answer
        