# 1. Two Sum (https://leetcode.com/problems/two-sum/)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        dic={}
        for i in range(0,len(nums)):
            if target-nums[i] in dic and dic[target-nums[i]]!=i:               
                return [i,dic[target-nums[i]]]
            else:
                dic.update({nums[i]:i})
     
        return []       