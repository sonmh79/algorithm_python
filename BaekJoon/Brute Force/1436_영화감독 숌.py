import sys

""" 
    문제: 6이 세 번이상 연속해야 한다.
    666부터 1씩 더해가며 6이 연속하는지 모두 탐색하고 만족하면 cnt += 1
    n == cnt이면 게임 끝 ~
    
"""

n = int(sys.stdin.readline())

cnt = 0 

i = 0
while True:
    num = 666 + i
    cnt_6 = 0
    for char in str(num):
        if char == "6":
            cnt_6 += 1
        
        else:
            cnt_6 = 0
        
        if cnt_6 >= 3:
            cnt += 1
            break
    
    if cnt == n:
        print(num)
        break

    i+=1