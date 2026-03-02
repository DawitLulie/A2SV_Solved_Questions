from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def goodsubarray(n):
            dic = Counter()
            left = 0
            subarray = 0

            for right in range(len(nums)):
                dic[nums[right]] += 1

                while len(dic) > n:
                    num = nums[left]
                    dic[num] -= 1
                    
                    if dic[num] == 0:
                        del dic[num]
                    left += 1

                subarray += (right - left + 1)

            return subarray

        return goodsubarray(k) - goodsubarray(k-1)


        
