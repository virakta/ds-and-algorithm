#Valid Palindrome

'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0;
        j=len(s)-1
        while(i<j):
            while i<j and not s[i].isalnum(): i+=1;
            while j>i and not s[j].isalnum(): j-=1;
            #print(i,j,s[i],s[j])
            if s[i].lower() != s[j].lower() :
                return False
            i+=1
            j-=1
        
        return True
        