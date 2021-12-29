import sys
from collections import defaultdict

"""
    딕셔너리에 {l:[word1,word2 ,,, wordn]} 형태로 저장한 후,
    출력 시 l에 대한 오름차순으로 출력하며 각 l이 value로 가지는 리스트를 정렬하여 출력한다.
"""

n = int(sys.stdin.readline())
d = defaultdict(list)

for _ in range(n):
    word = str(sys.stdin.readline().strip("\n"))
    l = len(word)
    if word not in d[l]:
        d[l].append(word)

for l in range(1,51):
    if len(d[l]) != 0:
        words = d[l]
        words.sort()
        for word in words:
            print(word)