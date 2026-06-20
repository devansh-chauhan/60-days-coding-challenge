def edit_distance_recursive(word1, word2, m, n):
    if m == 0:
        return n

    if n == 0:
        return m

    if word1[m - 1] == word2[n - 1]:
        return edit_distance_recursive(word1, word2, m - 1, n - 1)

    return 1 + min(
        edit_distance_recursive(word1, word2, m, n - 1),     
        edit_distance_recursive(word1, word2, m - 1, n),     
        edit_distance_recursive(word1, word2, m - 1, n - 1)   
    )


def edit_distance_dp(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     
                    dp[i][j - 1],     
                    dp[i - 1][j - 1]   
                )

    return dp[m][n], dp


word1 = "horse"
word2 = "ros"
distance, table = edit_distance_dp(word1, word2)
print("Word 1:", word1)
print("Word 2:", word2)
print("\nMinimum Edit Distance:", distance)
print("\nDP Table:")
for row in table:
    print(row)