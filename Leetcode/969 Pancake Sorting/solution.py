class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []

        for i in range(n):
            max_val = -1
            index = -1

            # find max in unsorted part
            for j in range(n - i):
                if arr[j] > max_val:
                    max_val = arr[j]
                    index = j

            # if already in correct position, skip
            if index == n - 1 - i:
                continue

            # flip max to front
            if index != 0:
                arr[:index+1] = arr[:index+1][::-1]
                result.append(index + 1)

            # flip to correct position
            arr[:n-i] = arr[:n-i][::-1]
            result.append(n - i)

        return result