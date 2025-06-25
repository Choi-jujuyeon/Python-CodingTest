class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        l,r=0,len(nums)-1     #인덱스 값저장

        while l<=r: #r이 계속 클동안
            if nums[l] < nums[r]:
                res=min(res,nums[l])
                break
            m=(l+r)//2 #피봇 값 인덱스 저장
            res=min(res,nums[m])
            
            if nums[m]>= nums[l]:
                l=m+1
            else:
                r=m-1
        return res

