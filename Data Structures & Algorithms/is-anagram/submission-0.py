class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_text1 = "".join(sorted(s))
        sorted_text2 = "".join(sorted(t))
        if len(s) == len(t):
            for i in range(len(s)):
                if sorted_text1[i] == sorted_text2[i]:
                    continue
                else:
                    return False
            return True
        return False