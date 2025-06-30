class Solution(object):
    def twoSum(self, nums, target):
        hashMap={} #값:인덱스

        for idx,num in enumerate(nums):
            t=target-num
            if t in hashMap:
                return [hashMap[t], idx]
            hashMap[num]=idx
        