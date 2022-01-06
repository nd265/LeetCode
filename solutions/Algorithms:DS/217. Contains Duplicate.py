# 217. Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)
# author: Navya Dahiya
# created: 18 Feb, 2021

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        s=set()
        for i in range(0,len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        