class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sol_1. hashMap
        # hashMap={}
        # for idx,num in enumerate(numbers):
        #     t=target-num
        #     if t in hashMap:
        #         return [hashMap[t]+1, idx+1]
        #     hashMap[num]=idx
        #sol_2. pointer        
        l,r=0,len(nums)-1
        while l<r:
            curSum= nums[l] + nums[r]
            
            # 값을 줄일경우: 오른쪽 포인터 (-)이동
            if curSum>target:
                r-=1
            # 값을 늘릴 경우: 왼쪽 포인터 (+)이동
            elif curSum < target:
                l+=1
            else:
                return [l+1, r+1]
            
