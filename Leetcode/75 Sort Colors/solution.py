class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick_sort(nums, left, right):
            if left >= right:
                return

            pivot = partition(nums, left, right)
            quick_sort(nums, left, pivot - 1)
            quick_sort(nums, pivot + 1, right)
        
        def partition(nums, left, right):
            pivot = nums[left]

            i = left + 1
            j = right

            while True:

                while i <= right and nums[i] < pivot:
                    i += 1
                
                while j > left and nums[j] >= pivot:
                    j -= 1
                
                if i > j:
                    break
                
                nums[i], nums[j] = nums[j], nums[i]

            nums[left], nums[j] = nums[j], nums[left]

            return j
        
        quick_sort(nums, 0, len(nums)-1)

        return nums
            
        
        