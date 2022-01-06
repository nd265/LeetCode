# 128. Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence)
# author: Navya Dahiya
# created: 16 Feb, 2021

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s=set()
        for i in range(0,len(nums)):
            s.add(nums[i])
        # print(s)
        longest=0
        large=0
        for i in s:
            current=i
            if current-1 in s:
                continue
            while current+1 in s:
                large+=1
                if large>longest:
                    longest=large
                current+=1    
            large=0
        return longest+1
                