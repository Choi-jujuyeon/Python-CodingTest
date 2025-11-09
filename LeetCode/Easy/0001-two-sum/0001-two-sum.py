class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={}

        for i,v in enumerate(nums):
            if target-v in preMap:
                return [i, preMap[target-v]]

            preMap[v]=i
            
