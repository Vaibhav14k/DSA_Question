class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        temp = numBottles

        while temp >= numExchange:
            new_bottles = temp//numExchange
            count += new_bottles
            temp = temp % numExchange + new_bottles
        return count

obj = Solution()
print(obj.numWaterBottles(9,3))