class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freq_list = []
        for num, count in counts.items():
            freq_list.append((count, num))
        
        freq_list.sort(key=lambda x: x[0], reverse=True)
        
        res = []
        for i in range(k):
            res.append(freq_list[i][1])
            
        return res