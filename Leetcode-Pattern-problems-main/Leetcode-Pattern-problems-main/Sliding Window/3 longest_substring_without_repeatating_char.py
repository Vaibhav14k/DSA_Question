class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        max_len = 0
        max_len_word = ''
        start = 0
        while (start<n):
            window_len =0
            window_len_word = ''
            for i in range(start,n):
                if s[i] not in window_len_word:
                    window_len_word += s[i]
                    window_len +=1
                    print("window length word-->",window_len_word," length-->",window_len)
                else:
                    break
            max_len = max(max_len,window_len)
            max_len_word = max(max_len_word,window_len_word)
            print("maximum length word-->",max_len_word," length-->",max_len)
            start+=1
        print(max_len_word)
        return max_len

s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))