'''
Given a string s, return the longest palindromic substring in s. 回文字符串
'''
# Violent O(n^3)
def isPalindrome(s):
    for i in range(len(s)//2):
        if(s[i]!=s[len(s)-i-1]):
            return False
    return True

def longestPalindrome_v(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub_s = s[i:j]
            if(isPalindrome(sub_s) and max_len<len(sub_s)):
                max_len = len(sub_s)
                ans = sub_s[:]
    return ans
# ----------------------------------------------------------------
# Dynamic planning O(n^2)
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    
    max_len = 1
    begin = 0
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    # print(dp)
    for i in range(n):
        dp[i][i] = True
    
    # 递推开始
    # 先枚举子串长度
    for L in range(2, n + 1):
        # 枚举左边界，左边界的上限设置可以宽松一些
        for i in range(n):
            # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
            j = L + i - 1
            # 如果右边界越界，就可以退出当前循环
            if j >= n:
                break

            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            
            # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i
    return s[begin:begin + max_len]


if __name__ == "__main__":
    print(longestPalindrome_v("1423214"))