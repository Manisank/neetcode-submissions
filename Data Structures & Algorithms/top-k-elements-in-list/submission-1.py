class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter


        # 1. Count frequencies O(n)
        count = Counter(nums)
        
        # 2. Bucket Sort: Create a list of arrays where the index represents the frequency
        # Max possible frequency is len(nums), so we need len(nums) + 1 buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. Gather the top k frequent elements by iterating backwards O(n)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result