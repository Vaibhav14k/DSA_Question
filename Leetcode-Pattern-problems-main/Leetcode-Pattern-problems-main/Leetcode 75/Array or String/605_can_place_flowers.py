class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        summ = sum(flowerbed)
        print(summ)
        i = 0
        while i<length-1:
            if i==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
            if flowerbed[i+1] == 0 and flowerbed[i-1] == 0 :
                flowerbed[i]=1
            i+=1
        if i==length-1 and flowerbed[i-1]==0:
            flowerbed[i]=1
        if(sum(flowerbed)-summ>=n):
            return True 
        else: 
            return False

obj = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(obj.canPlaceFlowers(flowerbed,n))

        