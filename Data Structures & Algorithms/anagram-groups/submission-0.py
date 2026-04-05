class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for data in strs:
            temp = "".join(sorted(data))

            if temp not in d:
                d[temp] = [data]
            else:
                d[temp].append(data)
        return list(d.values())