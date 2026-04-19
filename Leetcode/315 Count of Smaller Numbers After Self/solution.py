class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        def merge(left, right):
            merged = []
            i = j = 0
            count = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    result[left[i][1]] += count
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += 1
                    j += 1
            
            while i < len(left):
                result[left[i][1]] += count
                merged.append(left[i])
                i += 1

            merged.extend(right[j:])
            return merged

        def merge_sort(arr):
            if len(arr) <= 1:  
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        arr = [[nums[i], i] for i in range(len(nums))]
        merge_sort(arr)

        return result