class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = sorted(nums);
        for i in range(len(nums) - 1):
            if li[i] == li[i+1]:
                return True

        return False