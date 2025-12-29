import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        n = len(words)
        if n<k:
            return words
        freq =list( Counter(words).items())
        heap = [(-frequency,word) for word,frequency in freq]
        heapq.heapify(heap)
        print(heap)
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result
obj = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 3
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(obj.topKFrequent(words,k))