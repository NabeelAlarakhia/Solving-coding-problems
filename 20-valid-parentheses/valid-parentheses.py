class Solution:
    def isValid(self, s: str) -> bool:
        # so we cant have ([)] for example
        #( must match with )
        # so we need to use a stack
        # if you push a parentheses into a stack and then its met with its closing then pop them
        # both out. If a different one occurs before the closing then push that to the top and 
        # check for that closing, and repeat
        # If the parenthesis is closed by another one then return false

        stack = []
        opening = {"(":1 , "{":2, "[":3}
        closing = {")":1 , "}":2 , "]":3}

        n = len(s)
        for i in s:
            if i not in closing:
                stack.append(i)
            else:
                if len(stack)>0:
                    pop_brac=stack.pop()
                    if closing[i]==opening[pop_brac]:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False          
        