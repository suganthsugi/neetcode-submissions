class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            while i<=j and not s[i].isalnum():
                i+=1
            while i<=j and not s[j].isalnum():
                j-=1
            if i>j:
                print(i, j)
                break
            val1 = s[i]
            val2 = s[j]
            if (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')):
                val1 = chr(ord(val1) - (ord('A')-ord('a')))
            if (ord(s[j])>=ord('A') and ord(s[j])<=ord('Z')):
                val2 = chr(ord(val2) - (ord('A')-ord('a')))
            if(val1==val2):
                i+=1
                j-=1
            else:
                return False
        return True