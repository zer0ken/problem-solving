class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        mid = len(merged) // 2
        if len(merged) % 2 == 1:
            return merged[mid]
        return (merged[mid] + merged[mid-1]) / 2