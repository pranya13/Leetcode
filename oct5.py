class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        ts = sum(ord(a) for a in s1)
        window_length = len(s1)
        for i in range(len(s2) - window_length + 1):
            window = s2[i:i + window_length]
            s = sum(ord(char) for char in window)
            if s == ts:
                if sorted(window) == sorted(s1):
                    return True 
        return False

