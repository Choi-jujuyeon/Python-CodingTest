class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        def backtracking(start):
            #base_case
            if len(arr) ==2:
                if nums[arr[0]] + nums[arr[1]] == target:
                    return arr[:]
                return False

            for i in range(start,len(nums)):                      
                arr.append(i)
                if backtracking(i+1):
                    return arr
                arr.pop()
        return backtracking(0)
        