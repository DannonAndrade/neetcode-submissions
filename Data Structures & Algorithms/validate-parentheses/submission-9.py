class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closed = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in closed:
                if stack:
                    if closed[c] == stack[-1]:
                        stack.pop()
                    elif c != stack[-1]: return False
                else: return False
            else:
                stack.append(c)
        
        if stack: return False
            
        return True
