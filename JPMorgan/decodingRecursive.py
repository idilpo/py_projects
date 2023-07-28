# strings starting with 0 is invalid
# can only take double-digit values if the first string starts with a 1 or 2:
# because up to 26 --> 1 can take 0-9, 2 can take 0-6
# O(n) since at any position i, we have at most two decisions to make = O(1) and we ask how can we decode the rest
# O(n) = size of the cache, memory and time complexity
# t any position i, we look at the two positions that come afer it to make a decision --> dp[i] = dp[i+1] + dp[i+2]

class resursiveSolution:

    def numDecodings(self, s: str) -> int:
        # base case: the entire length of the str maps to 1 bc if an empty str is given, we want to return 1
        dp = {len(s) : 1}

        # recursive function:
        def dfs(i):
            # base cases:
            if i in dp: # i is either already been cached or is the last position
                return dp[i]
            if s[i] == "0": # if the string is starting with a 0
                return 0

            # recursive case:
            res = dfs(i+1)
            if ((i+1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                # if there is another char after i (i+1 < len(s)) and s starts with 1 or
                # s starts with 2 and the following char is less than 7
                res += dfs(i+2) # subproblem is i+2 bc it is a double-digit number
            dp[i] = res# caching the result
            return res

        return dfs(0) # we want to know how many ways we csn decode this string starting at index 0