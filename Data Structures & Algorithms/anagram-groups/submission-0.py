class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for index in strs:
            sortedindex = ''.join(sorted(index))
            hashmap[sortedindex] = hashmap.get(sortedindex, []) + [index]
        return list(hashmap.values())