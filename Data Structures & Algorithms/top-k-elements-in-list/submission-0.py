class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else: 
                my_dict[num] += 1 
        sorted_mydict = dict(sorted(my_dict.items(), key = lambda item:item[1], reverse = True))
        counter = 0
        answer = []
        for n in sorted_mydict:
            if counter < k:
                answer.append(n)
                counter += 1
            else:
                return answer
        return answer

