class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for idx,n in enumerate(nums):
            #같은 값을 2번 사용할 생각 없음
            if idx>0 and n==nums[idx-1]:
                continue
            
            l,r=idx+1, len(nums)-1
            while l<r:
                threeSum = n+ nums[l]+nums[r]
                if threeSum >0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

        return res  