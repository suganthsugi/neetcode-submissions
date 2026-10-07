class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = math.inf
        left, right = 0, len(nums)-1

        while nums[left]>nums[right]:
            mid = math.floor((right-left)/2)+left
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1
        
        return min(result, nums[left])