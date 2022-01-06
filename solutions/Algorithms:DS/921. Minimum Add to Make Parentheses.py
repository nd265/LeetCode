# 921. Minimum Add to Make Parentheses Valid (https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
# author: Navya Dahiya
# created: 16 Feb, 2021

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        dic={'(':0,')':0}
        if not S:
            return 0
        for i in S:
            if i=='(':
                dic['(']+=1
            elif i==')' and dic['(']>0:
                dic['(']-=1
            else:
                dic[i]+=1
        return dic['(']+dic[')']   