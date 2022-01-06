# 268. Missing Number (https://leetcode.com/problems/missing-number/)
# author: Navya Dahiya
# created: 18 Feb, 2021

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        sum=int((l*(l+1))/2)
        
        arraysum=0
        for i in range(0,len(nums)):
            arraysum+=nums[i]
        
        return sum-arraysum
        