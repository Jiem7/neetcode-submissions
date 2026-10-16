class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix=[1]*(length+1)
        prefix[1] = nums[0]
        suffix=[1]*(length+1)
        suffix[-2] = nums[-1]
        answer = [1]*length
        for i in range(1, length):
            prefix[i+1] = prefix[i] * nums[i]
            suffix[-(i+2)] = suffix[-(i+1)] * nums[-(i+1)]
        for i in range(length):
            answer[i] = prefix[i]*suffix[i-length]
        return answer
        