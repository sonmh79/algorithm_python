import sys

n = int(sys.stdin.readline())

ans = []
for num in range(1,n):
    sum = num
    for i in str(num):
        sum += int(i)
    if sum == n:
        ans.append(num)

if ans == []:
    print(0)
else:
    print(min(ans))