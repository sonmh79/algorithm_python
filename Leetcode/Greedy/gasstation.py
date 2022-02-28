class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        """ 원형 주유소 돌기 (정답은 오직 하나) """
        
        # 총 가스량 보다 비용이 더 크면 돌기 불가능
        if sum(gas) < sum(cost):
            return -1
        
        # 처음부터 탐색하되 , 연료가 바닥나면 정답이 아님
        fuel,start = 0,0 
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            
            else:
                fuel += gas[i] - cost[i]
                
        return start
