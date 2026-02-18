class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = Counter()
        arr = nums.copy()
        arr.sort()

        for i in range(len(nums)):
            if i > 0 and arr[i] == arr[i-1]:
                dic[arr[i]] = dic[arr[i-1]]
            else:
                dic[arr[i]] = i
                
        result = []
        for num in nums:
            result.append(dic[num])

        return result


         

















