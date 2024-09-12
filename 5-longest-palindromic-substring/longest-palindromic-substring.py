class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s
        
        start, maxl = 0, 1  # To keep track of the start index and length of the longest palindrome

        dp = [[False] * n for _ in range(n)]  # Create a 2D DP table
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for two-character palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxl = 2
                start = i
        
        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):  # Length of the substring
            for i in range(n - length + 1):  # Starting index of the substring
                j = i + length - 1  # Ending index of the substring
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    maxl = length
                    start = i
        
        # Return the longest palindrome substring
        return s[start:start + maxl]
