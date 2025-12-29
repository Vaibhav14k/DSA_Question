class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0
        
        s = ""
        i = 0
        
        while i < n:
            char = chars[i]
            count = 0
            
            while i < n and chars[i] == char:
                i += 1
                count += 1
            
            s += char
            
            if count > 1:
                s += str(count)
        
        for i in range(len(s)):
            chars[i] = s[i]
        
        return len(s)

obj = Solution()
chars = ["a","a","b","b","c","c","c"]
print(obj.compress(chars))