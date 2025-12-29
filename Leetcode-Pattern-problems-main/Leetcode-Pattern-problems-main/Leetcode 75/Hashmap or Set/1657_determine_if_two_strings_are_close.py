from typing import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        print(count1)
        print(count2)
        count1 = list(count1.values())
        count2 = list(count2.values())
        count1.sort()
        count2.sort()
        print(count1)
        print(count2)
        for i in range(len(count1)):
            if count1[i]!=count2[i]:
                return False
        return True



obj = Solution()
word1 = "abc"
word2 = "bca"
word1 ="abbzzca"
word2 ="babzzcz"
# word1 = "abbzccca"
# word2 ="babzzczc"
print(obj.closeStrings(word1,word2))