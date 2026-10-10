class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        out = []
        for i, n in enumerate(strs):
            n = "".join(sorted(n))
            if n not in hash_map:
                hash_map[n] = [i]
            else:
                hash_map[n].append(i)
        for idxs in hash_map.values():
            out.append([strs[i] for i in idxs])
        return out
                