class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            count=0
            while i:
                i=i&(i-1)
                count+=1
            res.append(count)
        return res