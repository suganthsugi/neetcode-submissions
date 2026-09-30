class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited_map = {}
        result = []

        for x in nums:
            if x in visited_map:
                visited_map[x]+=1
            else:
                visited_map[x] = 1
        
        t=set(sorted(list(visited_map.values()), reverse=True)[:k])
        for x in visited_map.keys():
            if visited_map[x] in t:
                result.append(x)
        return result
