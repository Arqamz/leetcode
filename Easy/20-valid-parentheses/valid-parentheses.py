class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue
            
            if not stack:
                return False

            if (c == ')' and stack[-1] == '(') or (c == '}' and stack[-1] == '{') or (c == ']' and stack[-1] == '['):
                stack.pop()
                continue
            else:
                return False

        if stack != []:
            return False

        return True