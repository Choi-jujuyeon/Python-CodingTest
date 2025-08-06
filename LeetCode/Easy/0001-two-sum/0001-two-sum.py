class Solution(object):
    def twoSum(self, nums, target):
        hashMap={}
        
        for i,n in enumerate(nums):
            if (target-n) in hashMap:
                return hashMap[target-n], i
            else:
               hashMap[n] =i
        
                
