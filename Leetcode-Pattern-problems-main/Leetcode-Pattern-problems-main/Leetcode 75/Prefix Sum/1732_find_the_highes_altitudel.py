class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        maxx = 0
        temp = 0
        for i in gain:
            temp +=i
            maxx = max(maxx,temp)
        return maxx

obj = Solution()
gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
print(obj.largestAltitude(gain))
