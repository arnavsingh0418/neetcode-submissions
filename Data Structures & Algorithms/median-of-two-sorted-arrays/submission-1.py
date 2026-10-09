class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # combined1 = nums1+nums2
        combined = sorted(nums1+nums2)
        cLen = len(combined)
        mid1 = (cLen // 2)-1
        mid2 = (cLen // 2)

        if(cLen & 1 == 0): #even
            return ((combined[mid1] + combined[mid2]) / 2)
        else:
            return combined[cLen//2]