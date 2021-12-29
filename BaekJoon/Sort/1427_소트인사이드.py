import sys

""" 
    주어진 수에서 0~9의 개수를 센다.
    9부터 0까지 나온 개수만큼 차례대로 출력한다.
"""

num = str(sys.stdin.readline()).strip("\n")

d = [0] * 10 # 0 ~ 9

for char in num:
    d[int(char)] += 1

ans = ""
for i in range(9,-1,-1):
    if d[i] != 0:
        ans += str(i) * d[i]

print(ans)