"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2]. 
"""
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        counts = []
        for i in range(0, num+1):
            counts.append(bin(i).count("1"))
            print("num of 1s: {}".format(bin(i).count("1")))
        return counts
