class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if min(nums) ==0:
            for i in range(min(nums), max(nums)+1):
                if i not in nums:
                    return i
            return max(nums) +1
        else:
            return 0