class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        arr=[]
        re=[]

        def backtracking():
            if len(arr) ==len(nums):
                re.append(arr[:])
            for i in nums:
                if i not in arr:
                    arr.append(i)
                    backtracking()
                    arr.pop()
        backtracking()
        return re