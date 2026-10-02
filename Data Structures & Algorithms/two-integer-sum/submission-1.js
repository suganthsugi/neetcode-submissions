class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const visitedMap = {}

        for(var i=0; i<nums.length; i++) {
            const need = target-nums[i]
            if(!Object.hasOwn(visitedMap, need)) {
                visitedMap[nums[i]] = i
            }
            else {
                return [visitedMap[need], i]
            }
        }
    }
}
