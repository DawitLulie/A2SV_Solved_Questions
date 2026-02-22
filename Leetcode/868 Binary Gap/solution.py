class Solution:
    def binaryGap(self, n: int) -> int:
        arr = []

        while n > 0:
            arr.append(n % 2)
            n //= 2

        left = 0
        gap = 0

        for right in range(len(arr)):
            if arr[right] == 1:
                while arr[left] != 1:
                    left += 1

                gap = max(gap, right - left)
                left = right
                
        return gap


