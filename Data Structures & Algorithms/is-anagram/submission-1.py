class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = sorted(s)
        t_set = sorted(t)

        return s_set == t_set
        