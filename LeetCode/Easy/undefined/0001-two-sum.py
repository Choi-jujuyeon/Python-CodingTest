class Solution(object):
    def twoSum(self, nums, target): 
        dict={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in dict:
                return [dict[diff], i]
            else:
                dict[nums[i]] = i
        