class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
         # Add open: if open <n
         # Add close: if close<open
         # valid(stop) open==close==n
        stack=[]    #임시저장
        res=[]

        def backtrack(openN,closedN):
            if n==openN ==closedN:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res
