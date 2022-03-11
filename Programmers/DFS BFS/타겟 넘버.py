def solution(numbers, target):
    """숫자별로 + 혹은 -의 연산을 가질 수 있기 때문에 이진 트리 구조의 DFS를 통해 모든 경우의 수를 계산해보고 target과 맞는 갯수 리턴"""
    answers = []

    def dfs(n,a):
    
        if n == len(numbers):
            if a == target:
                answers.append(a)
            return 
    
        dfs(n+1,a+numbers[n])
        dfs(n+1,a-numbers[n])

    dfs(0,0)
    return(len(answers))