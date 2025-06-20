class Solution:
    def fib(self, n: int) -> int:
        one,two = 1,0
        if n==0:
            return two
        elif n==1:
            return one
        else:
            for i in range(n-1):
                temp=one+two
                two=one
                one=temp
            return one