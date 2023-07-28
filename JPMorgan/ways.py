"""
a given index, we can decode in two ways:
1. as itself
2. as a pair with the previous number

input = 1 --> ways = 1
input = 12 --> ways = 2 (1&2, 12)
input = 121 --> ways = 3 (1&2&1, 1&21, 12&1)
input = 1212 --> ways = 5 (1&2&1&2, 12&1&2, 1&21&2, 1&2&12, 12&12)
input = 12121 --> ways = 8 (1&2&1&2&1, 12&1&2&1, 1&21&2&1, 1&2&12&1, 12&12&1, 1&21&21, 1&2&1&21, 12&1&21)

ways[i] = ways[i-1] + ways[i-2]

case 1 - number of i and i-1 between 10-26: ways[i] = ways[i-1] + ways[i-2]
case 2 - number of i and i-1 larger than 26: ways[i] = ways[i-1]
case 3 - number of i==0 and i-1==1 or i-1==2: ways[i] = ways[i-2]
case 4 - number of i==0 and i-1>2: return 0 (invalid)
"""

# Brute Force Solution:
# time - O(2^n), space - O(n)
def solution(encoding):
    return helper(encoding)

def helper(sub_encoding):
    sub_encoding_length = len(sub_encoding)
    if sub_encoding_length == 0:
        return 1
    if sub_encoding_length == 1:
        if sub_encoding[0] == '0':
            return 0
        else:
            return 1

    last_number = sub_encoding[sub_encoding_length-1]
    second_last_number = sub_encoding[sub_encoding_length-2]
    if last_number == '0':
        if second_last_number == '1' or second_last_number == '2':
            return helper(sub_encoding[0:sub_encoding_length-2])
        else:
            return 0

    if (second_last_number == '1') or (second_last_number == '2' and int(last_number) < 7):
        return helper(sub_encoding[0:sub_encoding_length-1]) + helper(sub_encoding[0:sub_encoding_length-2])
    return helper(sub_encoding[0:sub_encoding_length-1])


# Memoization Solution:
# time - O(n), space - O(n)
def solutionM(encoding):
    memo = [-1 for i in range(len(encoding) + 1)]
    return helperM(encoding, memo)


def helperM(sub_encoding, memo):
    sub_encoding_length = len(sub_encoding)
    if sub_encoding_length == 0:
        return 1
    if sub_encoding_length == 1:
        if sub_encoding[0] == '0':
            return 0
        else:
            return 1
    if memo[sub_encoding_length] != -1:
        return memo[sub_encoding_length]

    last_number = sub_encoding[sub_encoding_length-1]
    second_last_number = sub_encoding[sub_encoding_length-2]
    if last_number == '0':
        if second_last_number == '1' or second_last_number == '2':
            memo[sub_encoding_length] = helperM(
                sub_encoding[0:sub_encoding_length-2], memo)
        else:
            memo[sub_encoding_length] = 0
        return memo[sub_encoding_length]

    if (second_last_number == '1') or (second_last_number == '2' and int(last_number) < 7):
        memo[sub_encoding_length] = helperM(
            sub_encoding[0:sub_encoding_length-1], memo) + helperM(sub_encoding[0:sub_encoding_length-2], memo)
    else:
        memo[sub_encoding_length] = helperM(
            sub_encoding[0:sub_encoding_length-1], memo)
    return memo[sub_encoding_length]


# Dynamic Programming Solution:
# time - O(n), space - O(n)
def solutionD(encoding):
    dp = [0 for _ in range(len(encoding) + 1)]
    dp[0] = 1
    if encoding[0] == '0':
        return 0
    else:
        dp[1] = 1

    for i in range(2, len(encoding) + 1):
        if encoding[i-1] == '0':
            if encoding[i-2] == '1' or encoding[i-2] == '2':
                dp[i] = dp[i-2]
            else:
                return 0
        else:
            if (encoding[i-2] == '1') or (encoding[i-2] == '2' and int(encoding[i-1]) < 7):
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] += dp[i-1]

    return dp[len(encoding)]