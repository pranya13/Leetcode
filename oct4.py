#Divide players into teams of equal skills
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill = sorted(skill)
        ts = skill[0] + skill[-1]
        s=0
        for i in range(len(skill)//2):
            if skill[i]+skill[-i-1] != ts:
                return -1
            s += skill[i] * skill[-1-i]   
            
        return s
        
