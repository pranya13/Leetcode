class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        stk = []
        for i in range(n):
            if not stk or nums[i]< nums[stk[-1]]:
                stk.append(i)
        for j in reversed(range(n)):
            while stk and nums[j]>= nums[stk[-1]]:
                i = stk.pop()
                ans = max(ans, j-i)
        return ans                
                      
        
