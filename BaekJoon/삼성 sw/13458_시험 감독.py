import sys

input = sys.stdin.readline

N = int(input())
classes = list(map(int, input().split()))
cap, sub = map(int, input().split())

answer = len(classes)

for students in classes:
    rest_students = students - cap
    if rest_students > 0:
        q, r = divmod(rest_students, sub)
        if r != 0:
            q += 1
        answer += q
print(answer)
