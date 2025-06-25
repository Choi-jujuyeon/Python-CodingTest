class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin, curMax=1,1 #곱하기에서 영향x
        
        for i in nums:
            if i==0:
                curMin,curMax=1,1
                
            temp=curMax
            curMax=max(i*curMax, i*curMin,i)
            curMin=min(i*temp, i*curMin,i)
            res=max(res,curMax)
        return res