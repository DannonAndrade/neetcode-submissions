class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opened = {'(': ')', '{': '}', '[': ']'}
        closed = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in opened:
                stack.append(opened[c])
            elif c in closed:
                if len(stack) > 0:
                    if c == stack[-1]:
                        stack.pop()
                    elif c != stack[-1]: return False
                else: return False
        
        if stack: return False
            
        return True
