# 242. Valid Anagram (https://leetcode.com/problems/valid-anagram/)
# author: Navya Dahiya
# created: 10 Feb, 2021

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1   
            else:
                dic.update({i:1})

        for j in t:
            if j in dic:
                dic[j]-=1   
            else:
                return False
        if all(v==0 for v in dic.values()):
            return True
