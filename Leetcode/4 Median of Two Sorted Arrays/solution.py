import bisect
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = (len(nums1) + len(nums2) - 1) // 2
        result = []

        # First binary search (left median)
        l = -10**6
        r = 10**6 + 1

        while r - l > 1:
            mid = (l + r) // 2
            cnt1 = bisect.bisect_left(nums1, mid)
            cnt2 = bisect.bisect_left(nums2, mid)

            if cnt1 + cnt2 > k:
                r = mid
            else:
                l = mid

        result.append(l)

        # Second binary search (right median)
        l = -10**6 - 1
        r = 10**6

        while r - l > 1:
            mid = (l + r) // 2
            cnt1 = len(nums1) - bisect.bisect_right(nums1, mid)
            cnt2 = len(nums2) - bisect.bisect_right(nums2, mid)

            if cnt1 + cnt2 > k:
                l = mid
            else:
                r = mid

        result.append(r)

        return sum(result) / 2