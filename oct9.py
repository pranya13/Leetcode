import math
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        um = 0
        stk = []
        for c in s:
            if c == '(':
                stk.append(c)
            elif c == ')':
                if stk:
                    stk.pop()
                else:
                    um+=1    
        return len(stk)+um                   
        
