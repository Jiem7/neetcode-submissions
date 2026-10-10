class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            to_find = target - nums[i]
            try:
                new = nums[i+1::]
                j = new.index(to_find) + (i+1)
            except ValueError:
                j = 0
            if j:
                return [i,j]
            