def longest_common_subsequence(text1, text2):
    dp = [[0 for row in range(len(text1) + 1)] for col in range(len(text2) + 1)]
    # print(dp)
    for row in range(len(text2) - 1, -1, -1):
        for col in range(len(text1) - 1, -1, -1):
            if text1[col] == text2[row]:
                dp[row][col] = 1 + dp[row + 1][col + 1]
            else:
                dp[row][col] = max(dp[row][col + 1], dp[row + 1][col])
    return dp[0][0]


text1 = "abcde"
text2 = "ace"

print(longest_common_subsequence(text1, text2))