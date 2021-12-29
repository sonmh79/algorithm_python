import sys
from collections import Counter


n = int(sys.stdin.readline())
numbers = []
summ = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    numbers.append(num)
    summ += num

numbers.sort()

# 평균
print(round(summ / n))
# 중앙값
print(numbers[n // 2])
# 최빈값
if n == 1:
    print(numbers[-1])
else:
    c = Counter(numbers).most_common(2)
    print(c[1][0] if c[0][1] == c[1][1] else c[0][0])
# 범위
print(numbers[-1] - numbers[0])
