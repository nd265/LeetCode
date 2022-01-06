# 169. Majority Element (https://leetcode.com/problems/majority-element/)
# author: Navya Dahiya
# created: 10 Feb, 2021

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for i in range(0, len(nums)):
            if nums[i] in dic:
                continue
            else:
                dic.update({nums[i]:0})
       
        
        res=int(len(nums)/2)
        
        for i in range(0, len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
                # return nums[i] if dic[nums[i]]>res
                
        
        for key in dic:
            if dic[key]>res:
                return key

