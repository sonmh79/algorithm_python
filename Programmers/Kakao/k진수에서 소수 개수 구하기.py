import math
def solution(n, k):
    
    def is_prime(num):
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    answer = 0
    result = ""
    while n >= k:
        n,r = divmod(n,k)
        if r == 0: 
            if result != "":
                if int(result) > 1 and is_prime(int(result)):
                    answer += 1
                result = ""
        else:
            result = str(r) + result
                
    result = str(n) + result
    if int(result) > 1 and is_prime(int(result)):
        answer += 1
    
    return answer