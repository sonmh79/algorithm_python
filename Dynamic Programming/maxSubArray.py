class Solution:

    """메모이제이션 방식, 배열의 누적합을 구하되, 누적합이 음수이면 더하지 않는다."""

    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        
        return max(nums)
    