from collections import Counter, defaultdict
class Solution:
    def minWindow(self,s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count = Counter(t)
        current_window_count = defaultdict(int)
        
        required = len(t_count)
        haved = 0
        
        left, right = 0, 0
        min_length = float("inf")
        min_window = ""
        
        while right < len(s):
            character = s[right]
            current_window_count[character] += 1
            print(current_window_count)
            if character in t_count and current_window_count[character] == t_count[character]:
                haved += 1
            
            while left <= right and haved == required:
                character = s[left]
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]
                
                current_window_count[character] -= 1
                if character in t_count and current_window_count[character] < t_count[character]:
                    haved -= 1
                left += 1
            right += 1
        
        return min_window

s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
print(obj.minWindow(s, t))