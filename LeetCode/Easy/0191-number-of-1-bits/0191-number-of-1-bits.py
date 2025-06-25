class Solution:
    def hammingWeight(self, n: int) -> int:
        count=Counter(bin(n)[2:])
        res=[v for k,v in count.items() if k=="1"]
        return res.pop()