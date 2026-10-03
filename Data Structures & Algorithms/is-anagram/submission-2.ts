class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const freqCount: Record<string, number> = {}
        if(s.length!==t.length) return false

        for(let i=0; i<s.length; i++) {
            if(!freqCount[s.charAt(i)]) {
                freqCount[s.charAt(i)] = 1
            } else {
                freqCount[s.charAt(i)] +=1
            }
            if(!freqCount[t.charAt(i)]) {
                freqCount[t.charAt(i)] = -1
            } else {
                freqCount[t.charAt(i)] -= 1
            }
        }
        for (let x of Object.values(freqCount)) {
            if(x!==0) {
                return false
            }
        }
        return true
    }
}
