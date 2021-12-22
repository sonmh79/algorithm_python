
def climbStairs(n) -> int:
        d = [0] * (n+1)
        d[1] = 1
        d[2] = 2
        print(d)
        
        if n == 1 or 2:
            return d[n]
        
        for i in range(3,n+1):
            d[i] = d[i-1] + d[i-2]
        
        print(d)
        return d[-1]
print(climbStairs(3))