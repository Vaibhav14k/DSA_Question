class Solution:
    def numberToWords(self, num: int) -> str:
        if str(num) == "0":
            return "Zero"
        num = str(num)
        n = len(num)
        map1 = {
        "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five",
        "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten",
        "11": "Eleven", "12": "Twelve", "13": "Thirteen", "14": "Fourteen", 
        "15": "Fifteen", "16": "Sixteen", "17": "Seventeen", "18": "Eighteen", "19": "Nineteen"
        }
        map2 = {
            "10": "Ten", "20": "Twenty", "30": "Thirty", "40": "Forty", 
            "50": "Fifty", "60": "Sixty", "70": "Seventy", "80": "Eighty", "90": "Ninety"
        }
        first = n%3 if n % 3 != 0 else 3 
        ans = []
        ans.append(num[:first])
        remaining = num[first:]
        for i in range(0,len(remaining),3):
            ans.append(remaining[i:i+3])

        res = ""
        count = len(ans) - 1
        for i in range(len(ans)):
            temp = ""
            length = len(ans[i])
            for j in range(length):
                if length - j == 3:
                    if ans[i][j] != "0":
                        temp += map1[ans[i][j]] + " Hundred "
                elif length - j == 2:
                    if ans[i][j] == "1":
                        temp += map1[ans[i][j:]] + " "
                        break 
                    elif ans[i][j] != "0":
                        temp += map2[ans[i][j] + "0"] + " "
                else:
                    if ans[i][j] != "0":
                        temp += map1[ans[i][j]] + " "
            if temp.strip():
                if count == 1:
                    res += temp + "Thousand"  + " "
                elif count == 2:
                    res += temp + "Million"  + " "
                elif count == 3:
                    res += temp + "Billion"  + " "
                else:
                    res += temp + " "
            count -= 1
        return res.strip() 
        


obj = Solution()
print(obj.numberToWords(1234567)) 
