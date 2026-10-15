class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans=[]
        for num in nums:
            product *= num
        for num in nums:
            if num != 0:
                ans.append(int(product/num))
            else:
                other_product = 1
                nums_copy = nums.copy()
                nums_copy.pop(nums.index(0))
                for num in nums_copy:
                    other_product *= num
                ans.append(other_product)
        return ans