"""
    1. n x n 크기의 2차원 리스트를 만든다. 원소는 "*"
    2. n x n 크기의 정사각형을 9등분 한다.
    3. 중앙의 정사각형 하나는 빈칸으로 채운다.
    4. 나머지 8개의 정사각형은 재귀함수를 돌린다.
    5. 크기가 1이 될때까지 2~4 반복 (재귀)
    6. 1에서 만든 리스트를 문자열로 통합해 출력한다.
"""

import sys

n = int(sys.stdin.readline())

d= []
for i in range(n): # 1
    d.append(["*"]*n)

def star(x,y,n):
    
    if n == 1: # 5
        return

    div_3 = n//3
    
    for i in range(0,n,div_3): # 2
        for j in range(0,n,div_3):
            if i == div_3 and j == div_3: # 3
                for r in range(div_3):
                    for c in range(div_3):
                        d[x+i+r][y+j+c] = " " # (x+i,y+j)는 전제 정사각형에서 현재 위치, (r,c)는 빈칸으로 만들 중앙 부분
            
            else: # 4
                star(x+i,y+j,div_3)
        
star(0,0,n)
                
for i in range(n): # 6
    row = ""
    for j in range(n):
        row += d[i][j]
    print(row)
