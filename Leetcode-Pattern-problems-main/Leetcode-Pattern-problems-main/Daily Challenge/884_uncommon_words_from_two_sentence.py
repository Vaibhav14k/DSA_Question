from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counter1 = Counter(s1.split())
        counter2 = Counter(s2.split())
        # print(counter1)
        # print(counter2)
        sol = []
        for val,count in counter1.items():
            if val not in counter2.keys() and count == 1:
                sol.append(val)
        for val,count in counter2.items():
            if val not in counter1.keys() and count == 1:
                sol.append(val)
        return sol

obj = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
# Output: ["sweet","sour"]
print(obj.uncommonFromSentences(s1,s2))