from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l=1
        while l<len(nums):
            if nums[l-1]==nums[l]:
                return True
            l+=1
        return False