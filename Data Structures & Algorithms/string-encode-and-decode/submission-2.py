class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "tite" + string
        return encoded    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            idx = s.find("tite", i)
            if idx == -1:
                break
            print(s[i])
            length = int(s[i:idx])
            start = idx + 4
            end = start + length
            decoded.append(s[start:end])
            i = end
        return decoded