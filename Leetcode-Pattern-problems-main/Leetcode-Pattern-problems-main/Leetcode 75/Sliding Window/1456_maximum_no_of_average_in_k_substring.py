class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        n = len(s)
        if n<k:
            for i in s:
                if i in vowels:
                    count +=1
            return count
        
        window = s[:k]
        temp = 0
        for i in window:
            if i in vowels:
                temp+=1
        count = temp
        # print(window,count)
        for i in range(k,n):
            # temp = 0
            # window = window[1:]+s[i]
            if s[i-k] in vowels:
                temp -=1
            if s[i] in vowels:
                temp +=1
            # print(window)
            # for i in window:
            #     if i in vowels:
            #         temp+=1
            count = max(count,temp)
        return count

obj = Solution()
s = "abciiidef"
k = 3
# s = "aeiou"
# k = 2
print(obj.maxVowels(s,k))