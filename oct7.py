class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while True:
            f= False
            if "AB" in s:
                s=s.replace("AB", '',1)
                f = True
            elif "CD" in s:
                s=s.replace("CD", '', 1)
                f=True
            if not f:
                break
            
        return len(s)   
            
        
