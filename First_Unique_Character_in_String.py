#First Unique Character in a String
'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        table={}
        for ch in s:
            if ch in table:
                table[ch]+=1
            else:
                table[ch]=1
                
        #python 3 by default dictory is ordered
        
        for key,val in table.items():
            if val==1 :
                return s.find(key) # Return the index in  orginal string
            
        
        return -1
        