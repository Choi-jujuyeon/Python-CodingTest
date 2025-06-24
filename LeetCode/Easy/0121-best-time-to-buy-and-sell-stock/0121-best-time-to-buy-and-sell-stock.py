class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #인덱스 취급
        maxP=0
        
        while r<len(prices):
            if prices[l]<prices[r]: #정상이익
                maxP=max(prices[r]-prices[l],maxP)
            else:
                l=r
            r+=1
        return maxP