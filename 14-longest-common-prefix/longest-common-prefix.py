class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hash_map = {}

        for char in strs:
            n = len(char)
            for i in range(n):
                prefix = char[:i+1]
                if prefix in hash_map:
                    hash_map[prefix] += 1
                else:
                    hash_map[prefix] = 1
        
        max_prefix = ""
        for prefix, count in hash_map.items():
            if count == len(strs) and len(prefix) > len(max_prefix):
                max_prefix = prefix
        
        return max_prefix
