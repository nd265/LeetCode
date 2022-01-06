# 136. Single Number (https://leetcode.com/problems/single-number/)
# author: Navya Dahiya
# created: 18 Feb, 2021

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #with extra space:
        # dic={}
        # for i in range(len(nums)):
        #     if nums[i] in dic:
        #         dic[nums[i]]+=1
        #     else:
        #         dic.update({nums[i]:0})
        # for key, value in dic.items():
        #     if value==0:
        #         return key 
        
        #without extra space and linear run time
     
        res=0
        for i in range(len(nums)):
            res=nums[i]^res
            
        return res
            