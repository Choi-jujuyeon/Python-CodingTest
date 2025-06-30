class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #sol_1. hashMap
        hashMap={}
        for idx,num in enumerate(numbers):
            t=target-num
            if t in hashMap:
                return [hashMap[t]+1, idx+1]
            hashMap[num]=idx
        