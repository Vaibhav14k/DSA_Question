class Solution:
    def minimumDeletions(self, s: str) -> int:
        if s.find("ba") == -1:
            return 0
        count_a = s.count("a")
        count_b = 0
        total = count_a
        for char in s:
            if char=="a":
                count_a -=1
            elif char=="b":
                count_b +=1
            total = min(total,count_a + count_b)
        return total

obj = Solution()
s = "aababbab"
print(obj.minimumDeletions(s))