class Solution:
    
    """ 1.Tabulation """
    
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 2:
            return n
        
        d = [0] * (n+1)
        d[1] = 1
        d[2] = 2
        
        for i in range(3,n+1):
            d[i] = d[i-1] + d[i-2]
        
        return d[-1]

from collections import defaultdict

class Solution:
    
    """ 2. Memoization """
    
    d = defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        if self.d[n]: # 계산 결과 저장
            return self.d[n]
        
        self.d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.d[n]
        
        