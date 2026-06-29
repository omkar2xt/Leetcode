class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        a = b = 0
        last = now = 0
        stop = (len(nums1) + len(nums2)) // 2

        for _ in range(stop + 1):

            last = now

            left = nums1[a] if a < len(nums1) else float("inf")
            right = nums2[b] if b < len(nums2) else float("inf")

            take_first = left <= right

            now = left if take_first else right

            a += take_first
            b += not take_first

        total = len(nums1) + len(nums2)

        return float(now) if total & 1 else (last + now) / 2.0