class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack=[]
        prefix=[0]
        res=0

        #누적합 체크
        for i in nums:
            prefix.append(prefix[-1]+i)
        
        #내림차순 발생 체크
        for i,n in enumerate(nums):
            newStart=i
            while stack and stack[-1][1]>n:
                idx,num = stack.pop()
                total = prefix[i] - prefix[idx]
                res = max(res,(total * num))
                newStart = idx
            stack.append((newStart,n))
        
        #스택에 남아 있을 경우
        for i,n in stack:
            total = prefix[len(nums)] - prefix[i]
            res = max(res,(total * n))

        return res % (10**9+7)

