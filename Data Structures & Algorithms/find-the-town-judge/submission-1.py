class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapping = { i:[] for i in range(1, n+1) }
        revMapping = { i:[] for i in range(1, n+1) }

        for i, j in trust:
            mapping[i].append(j)
            revMapping[j].append(i)

        for x in mapping.keys():
            if mapping[x]==[] and len(revMapping[x])==n-1:
                return x
        return -1