class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, closed, s):
            #valid answer
            if len(s) == n * 2: res.append(s)
            #add open
            if open < n: backtrack(open + 1, closed, s + "(")
            #add closing
            if cloes < open: backtrack(open, closed, s + ")")
        
        backtrack(0, 0)
        return res
    #--------------------------------------------------
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open, closed):
            #valid answer
            if open == closed == n:
                res.append("".join(stack))

            #add open
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()

            #add closing
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
