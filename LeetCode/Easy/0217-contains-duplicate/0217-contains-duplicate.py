from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr=list(Counter(nums).values())
        for i in arr:
            if i>1:
                return True
        return False