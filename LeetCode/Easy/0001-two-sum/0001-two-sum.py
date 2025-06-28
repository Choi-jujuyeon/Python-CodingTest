class Solution(object):
    def twoSum(self, nums, target):
        hashMap={}
        for idx,num in enumerate(nums):
            temp= target-num
            if temp in hashMap:
                return [hashMap[temp],idx]
            
            hashMap[num] = idx
        return hahsMap