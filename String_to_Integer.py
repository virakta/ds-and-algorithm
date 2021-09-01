# String to Integer (atoi)
'''
The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        table={'0':0,'1':1,'2':2,'3':3,'4':4 ,'5':5, '6':6, '7':7, '8':8, '9':9}
        s=s.lstrip(' ')
        i=0
        neg=0
        if s=="": return 0
        if s[i]=='-' :
            neg=1
            i+=1
        elif s[i]=='+': i+=1
        num=0
        while(i<len(s) and s[i] in table):
            digit=table[s[i]]
            num=num*10+digit
            i+=1
            
        if neg:
            num=num*-1
            if num < -(2**31):
                num=-(2**31)
                
        else:
            if num > (2**31-1):
                num= (2**31-1)
                
        return num