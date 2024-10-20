class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        log = []
        
        pure_bool = {'f', 't'}

        logic = {'|','!','&'}


        for char in expression:

            if char in pure_bool:
                stack.append(char == 't')

            elif char in logic:
                stack.append(char)
                log.append(char)

            elif char == ')':

                logic_subexpr = log.pop()

                if logic_subexpr == '!':
                    stack[-1] = not stack.pop()
                    continue
                

                while type(stack[-2]) is bool:
                    if logic_subexpr == '&':
                        stack[-1] = stack.pop() and stack[-1]

                    else:
                        stack[-1] = stack.pop() or stack[-1]

                stack[-1] = stack.pop()

        return stack[0]