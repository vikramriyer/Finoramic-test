class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        A.strip()
        operators = ['+', '-', '*', '/']
        stack = []

        for x in A:
            if x == '(' or x in operators:
                stack.append(x)
            elif x == ')':
                if stack[-1] in operators:
                    stack.pop()
                    stack.pop()
                else:
                    return 1
        return 0
