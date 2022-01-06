# 20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
# author: Navya Dahiya
# created: 10 Feb, 2021

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        dic={")":"(",
             "}":"{",
             "]":"["
             }
#         if len(s)==1 :
#             return False
       
        for i in range(0,len(s)):
           
            if s[i] in dic.values():
           
                stack.append(s[i])
               
            elif s[i] in dic.keys() and len(stack)>0 and stack[len(stack)-1]==dic[s[i]]:
                stack.pop()
            elif s[i] in dic.keys() and len(stack)==0 or  stack[len(stack)-1]!=dic[s[i]] :
                return False
                
            else:
                continue
                
          
        if not stack:
            return True
        else:
            return False
