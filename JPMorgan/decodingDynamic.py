class dynamicSolution():

    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        # starting at the end of the string and iterating in reverse:
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else: # a digit 1-9
                dp[i] = dp[i+1] # same as calling dfs(i+1) in recursive
            if ((i+1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]