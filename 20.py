"""
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.    
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={']':'[',')':'(','}':'{'}
        if len(s)%2==1:
            return False
        else:
            A=[]
            for i in s:
                if i not in d:
                        A.append(i)
                else:
                    if not A:
                        return False
                    if d[i]==A[-1]:
                        A.pop()
                    else:
                        return False
            return len(A)==0
