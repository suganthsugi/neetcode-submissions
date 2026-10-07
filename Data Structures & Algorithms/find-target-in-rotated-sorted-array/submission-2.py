class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:
            mid = math.floor((right-left)/2)+left

            if nums[mid]==target:
                return mid
            
            if nums[mid]>=nums[left]:
                if target>=nums[left] and target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if (target>=nums[left] and target>nums[mid]) or (target<nums[mid] and target<nums[right]):
                    right=mid-1
                else:
                    left = mid+1
        
        return -1
        