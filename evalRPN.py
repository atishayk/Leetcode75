from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        opr = ['+', '-','*','/']

        for x in tokens:
            if x not in opr:
                stack.append(int(x))
            else:
                b = (stack.pop())
                a = (stack.pop())
                if x == '+':
                    val = a + b
                    stack.append(val)
                elif x == '-':
                    val = a - b
                    stack.append(val)
                elif x == '*':
                    val = a * b
                    stack.append(val)
                else: # '/'
                    val = int(a / b)
                    stack.append(val)
        
        return stack[0]

            
