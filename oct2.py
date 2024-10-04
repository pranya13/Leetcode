#Rank transform in array
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = list(sorted(set(arr)))
        for i in range(len(arr)):
            arr[i] = bisect_left(ranks, arr[i]) + 1
        return arr
