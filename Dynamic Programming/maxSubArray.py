class Solution:
    
    """ O(n), 메모이제이션: 앞에서부터 계속 값을 계산하며 누적 합 구하고 0 이하면 버린다. """
    
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        
        return max(nums)

import sys
class Solution:
    
    """ 카데인 알고리즘 O(n), 매번 최댓값을 구함 """
    
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = 0
        best_sum = -sys.maxsize
        
        for num in nums:
            current_sum = max(num, num+current_sum)
            best_sum = max(current_sum, best_sum)
        
        return best_sum
        