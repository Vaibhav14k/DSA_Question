class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for i in details:
            if int(i[11:13])>60:
                count+=1
        return count
                

obj = Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(obj.countSeniors(details))  
'''
The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
'''