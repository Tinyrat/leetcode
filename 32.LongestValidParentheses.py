class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        stack = []
        begin = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    begin = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ret = max(ret, i - begin)
                    else:
                        ret = max(ret, i - stack[len(stack) - 1])
        return ret
