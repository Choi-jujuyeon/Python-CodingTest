class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin,curMax=1,1
        res=max(nums) #원소 수 1개인게 -1 이런거일 수 있음
        
        for n in nums:
            if n==0:
                curMin,curMax = 1,1
                continue
            temp=curMax
            curMax = max(n*curMin, n, n*curMax)
            curMin = min(n*temp,n,n*curMin)
            res=max(curMax,res)
        return res