t = int(input())


def main():
    m = int(input())
    nums = list(map(int, input().split()))

    operations = 0

    def merge(left, right):
        nonlocal operations

        if left[0] < right[0]:
            return left + right

        operations += 1
        return right + left


    def merge_sort(nums):
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2

        left = merge_sort(nums[:mid])
        right = merge_sort(nums[mid:])

        return merge(left, right)

    merged = merge_sort(nums)

    for i in range(1, m):
        if merged[i] <= merged[i - 1]:
            print(-1)
            return

    print(operations)


for _ in range(t):
    main()
    

    
