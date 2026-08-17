class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums);
        li = sorted(nums);
        for i in range(l-1):
            if li[i] == li[i+1]:
                return True

        return False