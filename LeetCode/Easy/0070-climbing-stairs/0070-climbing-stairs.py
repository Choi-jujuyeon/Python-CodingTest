class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        count=0
        for i in range(n-1):
            temp = one+two
            two=one
            one=temp
        return one