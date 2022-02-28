# import collections

# 1. Counter 사용
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         c = collections.Counter(nums)
#         return c.most_common(1)[0][0]

# 2. 파이썬 다운 방식
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return sorted(nums)[len(nums)//2]

# 3. 분할 정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return nums[-1]
        
        # 분할
        n = len(nums) // 2
        a = self.majorityElement(nums[:n])
        b = self.majorityElement(nums[n:])
        
        # 정복 - 과반수 조건이 있기 때문에 가능
        return [b,a][nums.count(a) > n]

# 속도는 1 > 3 > 2 으로 파이썬 다운 방식이 가장 빨랐다..
