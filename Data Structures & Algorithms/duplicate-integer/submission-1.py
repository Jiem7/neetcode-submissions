class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = []
        for num in nums:
            if num in cache:
                return True
            else:
                cache.append(num)
                continue
        return False