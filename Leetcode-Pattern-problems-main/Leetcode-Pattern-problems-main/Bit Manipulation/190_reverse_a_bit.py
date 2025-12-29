class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for _ in range(32):
            last_bit = n&1
            reverse = (reverse << 1) | last_bit
            n >>=1
        return reverse

n = 0b00000010100101000001111010011100
obj = Solution()
print(obj.reverseBits(n))