# 448. Find All Numbers Disappeared in an Array (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
# author: Navya Dahiya
# created: 18 Feb, 2021

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]>0:
                nums[index]*=-1
           
        for i in range(len(nums)):
            if nums[i]>0:
                missing.append(i+1)
        return missing