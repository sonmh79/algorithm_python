class Solution:
    
    """ Tabulation - i번째값 + i-2번째까지 최댓값 vs i-1번째까지 최댓값 """
    
    def rob(self, nums: List[int]) -> int:
        
        # 예외 처리
        if len(nums) <= 2:
            return max(nums)
        
        nums[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            nums[i] = max(
                nums[i] + nums[i-2], nums[i-1]
            )
        
        return nums[-1]