class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const freqCount = {}

        for(let i=0; i<nums.length; i++) {
            const x = nums[i]
            const need = target - x
            if(freqCount[need]===undefined) {
                freqCount[x] = i
            } else {
                return [freqCount[need], i]
            }
        }
    }
}
