class Solution:
    def findComplement(self, num: int) -> int:
        '''org = bin(num)[2:]
        print(org)
        ans = ""
        for i in range(len(org)):
            if org[i] == "1":
                ans += "0" 
            else:
                ans += "1" 
        return int(ans,2)'''
        return num ^ int (('1' * len(bin(num)[2:])),2)

obj = Solution()
print(obj.findComplement(5))  # Output: 2
print(obj.findComplement(2)) 