class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i, st in enumerate(strs):
            key = tuple(sorted(st))

            if key in seen:
                seen[key].append(st)
            else:
                seen[key] = [st]

        return list(seen.values())
