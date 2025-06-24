class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in Counter(nums).values():
            if i >=2: return True
        return False