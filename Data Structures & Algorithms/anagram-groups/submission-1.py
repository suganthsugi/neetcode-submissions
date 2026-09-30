class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = {}
        for x in strs:
            x_id = []
            for i in range(0, 26):
                x_id.append(0)
            
            for s in x:
                x_id[ord(s)-ord('a')] += 1
            
            x_id_str = '#'.join(map(str, x_id))
            if x_id_str in result_map:
                result_map[x_id_str].append(x)
            else:
                result_map[x_id_str] = [x]
        
        return list(result_map.values())