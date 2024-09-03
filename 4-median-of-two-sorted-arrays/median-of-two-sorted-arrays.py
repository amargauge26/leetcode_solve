class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = nums1 + nums2
        merged_list.sort()
        l = len(merged_list)
        if l % 2 == 0:
            return (merged_list[l // 2] + merged_list[(l // 2) - 1]) / 2.0
        else:
            return float(merged_list[l // 2])
