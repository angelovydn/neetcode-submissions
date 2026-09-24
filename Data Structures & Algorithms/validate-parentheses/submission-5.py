class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        chars = {')':'(',']':'[','}':'{'}

        for c in s:
        
            print(stack)

            if chars.get(c,0) and stack: # We encounter a closing brace
                if chars[c] == stack[-1]: 
                    stack.pop(-1) 
                else: return False # Most recently added was not the corresponding open brace
            
            else:
                stack.append(c)
        
        return False if stack else True

                