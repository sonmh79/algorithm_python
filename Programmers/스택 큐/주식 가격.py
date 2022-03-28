from collections import deque

def solution(prices):
    answer = []
    q = deque([[i,prices[i]] for i in range(len(prices))])
    while q:
        i,p = q.popleft()
        flag = True
        for post_i,post_p in q:
            if p > post_p:
                flag = False
                answer.append(post_i-i)
                break
        if flag:
            answer.append(len(q))

    return answer

print(solution([1,2,3,2,3]))