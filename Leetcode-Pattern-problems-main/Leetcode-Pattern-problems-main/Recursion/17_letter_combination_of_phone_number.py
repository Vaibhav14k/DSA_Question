class Solution:
    def solve(self,digits,ans,op,index,phone):
        if index == len(digits):
            ans.append(op)
            return
        num = int(digits[index]) 
        value = phone[num]
        print("num-->",num,"val-->>",value)
        for i in range(len(value)):
            self.solve(digits,ans,op + value[i],index+1,phone)
        
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        ans = []
        op = ""
        index = 0
        phone = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.solve(digits,ans,op,index,phone)
        return ans

obj = Solution()
print(obj.letterCombinations("23"))