class Solution:
    def calculate(self, s: str) -> int:
        def read(s):
            ans = []
            i = 0
            while i < len(s):
                if s[i] == " ":
                    i += 1
                elif s[i] in "()+-*/":
                    if s[i] == "-":
                        if i == 0 or (ans and ans[-1] == "("):
                            ans.append("0")
                    ans.append(s[i])
                    i += 1
                else:
                    number = ""
                    while i < len(s) and s[i].isdigit():
                        number += s[i]
                        i += 1
                    ans.append(number)
            return ans    
        def infixToPostfix(infix):
            #lowest -> highest
            stack = []
            #highest -> lowest
            postfix = []

            priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2} 

            for token in infix:
                if token == "(":
                    stack.append(token)
                elif token == ")":
                    while stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif token not in "+-/*":
                    postfix.append(token)
                else:
                    while stack and priority[stack[-1]] >= priority[token]:
                        postfix.append(stack.pop()) 
                    stack.append(token)

            while stack:
                postfix.append(stack.pop())

            return postfix
        def evaluatePostfix(postfix): 
            stack = []
            for i in postfix:
                if i not in "+-*/":
                    stack.append(int(i))
                else:
                    if len(stack) > 1:
                        b, a = stack.pop(), stack.pop()
                    else:
                        continue
                    if i == "+":
                        result = a + b
                    elif i == "-":
                        result = a - b
                    elif i == "*":
                        result = a * b
                    elif i == "/":
                        result = a / b
                    stack.append(int(result))

            return stack[-1]

        return evaluatePostfix(infixToPostfix(read(s)))
