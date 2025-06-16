class Solution(object):
    def twoSum(self, nums, target): 
        D={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in D:
                return [D[diff], i]
            else:
                D[nums[i]] = i
        