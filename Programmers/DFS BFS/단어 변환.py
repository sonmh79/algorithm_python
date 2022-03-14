def solution(begin, target, words):
    trip = [(0,begin)]
    visited = []
    
    while trip:
        cnt, node = trip.pop(0)
        if node == target:
            return cnt
        if node not in visited:
            visited.append(node)
            for word in words:
                t = 0
                for i in range(len(word)):
                    if word[i] != node[i]:
                        t += 1
                if t == 1:
                    trip.append((cnt+1,word))
    return 0

"""
bfs를 이용한 풀이
"""