class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                p, q = stack.pop(), stack.pop()
                stack.append(q - p)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                p, q = stack.pop(), stack.pop()
                stack.append(int(q / p))
            else:
                stack.append(int(t))
        return stack[0]