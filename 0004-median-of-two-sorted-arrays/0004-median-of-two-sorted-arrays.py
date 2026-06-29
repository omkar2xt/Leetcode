class Solution(object):
    def kth(self, A, B, k):
        if not A:
            return B[k]
        if not B:
            return A[k]

        ia = len(A) // 2
        ib = len(B) // 2

        ma = A[ia]
        mb = B[ib]

        if ia + ib < k:
            if ma < mb:
                return self.kth(A[ia + 1:], B, k - ia - 1)
            else:
                return self.kth(A, B[ib + 1:], k - ib - 1)
        else:
            if ma < mb:
                return self.kth(A, B[:ib], k)
            else:
                return self.kth(A[:ia], B, k)

    def findMedianSortedArrays(self, nums1, nums2):
        total = len(nums1) + len(nums2)

        if total % 2:
            return float(self.kth(nums1, nums2, total // 2))

        left = self.kth(nums1, nums2, total // 2 - 1)
        right = self.kth(nums1, nums2, total // 2)

        return (left + right) / 2.0