class Solution:
    def hammingWeight(self, n: int) -> int:
        # num = bin(n)[2:]
        # return num.count("1")
        count = 0
        while n:
            count += n&1
            n >>= 1
        return count


obj = Solution()
print(obj.hammingWeight(11))