class Solution:
    def isPalindrome(self,s:str,start:int,end:int) -> bool:
        n = len(s) 
        prefix_sum = [[0 for _ in range(26)] for _ in range(n+1)]
        # Building prefix sum array
        for i in range(n):
            prefix_sum[i+1][ord(s[i]) - ord("a")] +=1
        print(prefix_sum)

        # Doing summation
        for i in range(26):
            for j in range(1,n+1):
                prefix_sum[j][i] +=  prefix_sum[j-1][i]
        print(prefix_sum)

        count = 0
        for i in range(26):
            # We are including start and end 
            temp = prefix_sum[end+1][i] - prefix_sum[start][i]
            if temp %2 != 0:
                count +=1
        # If odd count letters are greater than 1 means palindrome can't be found
        if count >1:
            return False
        else:
            return True

obj = Solution()
s = "abaccde"
start,end = 1,2
start,end = 3,3
print(obj.isPalindrome(s,start,end))
