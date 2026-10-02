class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const visited = new Set()
        for(let x of nums) {
            if(visited.has(x)) {
                return true
            }
            else {
                visited.add(x)
            }
        }
        return false
    }
}
