class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        # 这段初始化先不管
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        # 求dp[i][j]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # 假如p[j]是 . 那么dp[i-1][j-1]能匹配 dp[i][j]就能匹配
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # 假如p[j]是 * 就比较复杂
                # 假如把 * 当作空，就要dp[i][j-1]匹配
                # 假如把 a* 当作空，就要dp[i][j-2]匹配
                # 假如要 a* 去匹配 a 就要dp[i-1][j-2]匹配且s[i]==p[j-1]
                # 假如是 .* 只要dp[i-1][j-2]匹配
                # dp[i-1][j-2]匹配等价于dp[i-1][j]匹配
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or \
                               (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                # 如果是字符，就要dp[i-1][j-1]匹配且s[i]==p[j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[len(s)][len(p)]
