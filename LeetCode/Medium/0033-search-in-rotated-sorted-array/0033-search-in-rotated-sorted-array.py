class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            
            #왼쪽일 경우
            if nums[l]<= nums[m]:
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1

            #오른쪽일 경우
            else:
                if target<nums[m] or target > nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1

        