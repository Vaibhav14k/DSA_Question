from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        freq = sorted(counter.values(),reverse=True)
        ans = 0
        count = 0
        for i,val in enumerate(freq):
            ans += ((i//8)+1) * val
        return ans
word = "xyzxyzxyzxyz"
word = "abcde"
word = "aabbccddeeffgghhiiiiii"
obj = Solution()
print(obj.minimumPushes(word))  