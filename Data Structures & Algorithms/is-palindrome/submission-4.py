class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            while i<=j and not ((ord(s[i])>=ord('0') and ord(s[i])<=ord('9')) or (ord(s[i])>=ord('a') and ord(s[i])<=ord('z')) or (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'))):
                i+=1
            while i<=j and not ((ord(s[j])>=ord('0') and ord(s[j])<=ord('9')) or (ord(s[j])>=ord('a') and ord(s[j])<=ord('z')) or (ord(s[j])>=ord('A') and ord(s[j])<=ord('Z'))):
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