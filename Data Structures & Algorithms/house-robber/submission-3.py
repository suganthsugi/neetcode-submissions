class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        h1, h2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            h1, h2 = h2, max(h1+nums[i], h2)
        return h2