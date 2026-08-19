# Let:
# n = number of strings
# k = average/max length of each string
# 
# Time Complexity: O(n × k)
# Space: O(n × k)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, st in enumerate(strs):
            count = [0] * 26

            for ch in st:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key in seen:
                seen[key].append(st)
            else:
                seen[key] = [st]

        return list(seen.values())
