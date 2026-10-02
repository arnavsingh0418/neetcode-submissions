class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["*", "-", "+", "/"]
        
        for i in range(len(tokens)):
            if tokens[i] in operators:
                a = stack.pop()
                b = stack.pop()
                if(tokens[i] == "+"):
                    stack.append(a+b)
                if(tokens[i] == "-"):
                    stack.append(b-a)
                if(tokens[i] == "*"):
                    stack.append(a*b)
                if(tokens[i] == "/"):
                    stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return int(stack[-1])