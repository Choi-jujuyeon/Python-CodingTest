class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsIdx= {num:idx for idx,num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack=[]

        for cur in nums2:
            while stack and cur>stack[-1]:
                res[numsIdx[stack.pop()]]=cur
            if cur in numsIdx:
                stack.append(cur)
        return res