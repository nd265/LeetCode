# 4. Median of Two Sorted Arrays (https://leetcode.com/problems/median-of-two-sorted-arrays)
# author: Navya Dahiya
# created: 10 Feb, 2021

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for n in nums2:
            nums1.append(n)
        # nums1.append(n for n in nums2)
        nums1.sort()
        print(nums1)
        length=len(nums1)
        if len(nums1)%2==0:
            index1=int(len(nums1)/2)-1
            index2=index1+1
            print (index1,index2)
            median= (nums1[index1]+nums1[index2])/2
            return median
        else:
            return nums1[int(len(nums1)/2)]