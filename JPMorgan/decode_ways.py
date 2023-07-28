
"""
Suppose we have a message containing letters from A to Z is being encoded to numbers using the following mapping −
'A' → 1, 'B' → 2 ... 'Z' → 26. So if we have one non-empty string, containing only digits, then we have to find,
in how many ways that can be decoded. So if the string is like “12”, then that can be made from “AB”, or “L”,
so there are two possible ways. So the answer will be 2.

To solve this, we will follow these steps − We will solve this using dynamic programming.
    n := length of s
    dp := an array with n number of 0s
    if s[0] is not ‘0’, then dp[0] := 1
    for i in range 1 to n – 1
        x := s[i] as integer, y := substring of s from index i – 1 to i + 1 as integer
        if x >= 1 and y <= 9, then dp[i] := dp[i] + dp[i – 1]
        if y >= 10 and y <= 26
        if i – 2 >= 0, then dp[i] := dp[i] + dp[i – 2], otherwise increase dp[i] by 1
    return last element of dp
"""

class Solution(object):
   def numDecodings(self, s):
      n = len(s)
      dp = [0 for i in range(n)]
      if s[0]!='0':
         dp[0]=1
      for i in range(1,n):
         x = int(s[i])
         y = int(s[i-1:i+1])
         if x>=1 and x<=9:
            dp[i]+=dp[i-1]
         if y>=10 and y<=26:
            if i-2>=0:
               dp[i]+=dp[i-2]
            else:
               dp[i]+=1
      return dp[-1]
ob1 = Solution()
print(ob1.numDecodings("226"))


"""
decode(encoding, error)

Parameters :
encoding : Specifies the encoding on the basis of which decoding has to be performed.
error : Decides how to handle the errors if they occur, e.g ‘strict’ raises Unicode error in case of exception and ‘ignore’ ignores the errors occurred.

Returns : Returns the original string from the encoded string.
"""

# decode()
str = "geeksforgeeks"

# encoding string
str_enc = str.encode(encoding="utf8")

# printing the encoded string
print("The encoded string in base64 format is: ", str_enc)

# printing the original decoded string
print("The decoded string is: ", str_enc.decode('utf8', 'strict'))


