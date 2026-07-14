class Solution(object):
    def isPalindrome(self, x):
      s = str(x)
      rev= ""
      for i in s:
          rev = i + rev
      if (rev==s):
            return True
      else:
            return False  
        