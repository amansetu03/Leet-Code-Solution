
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        st = 0
        max_length = 1

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                st = i
                max_length = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if length > max_length:
                        st = i
                        max_length = length

        return s[st:st + max_length]


def test(arr):
    s = Solution()
    for i in arr:
        print(f"s = \"{i}\", output = {s.longestPalindrome(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = ["babad","cbbd"]
        test(arr)
    else:
        S = Solution()
        print("enter number of test case: ")
        for _ in range(int(input())):
            s = input()
            print(f"s = \"{s}\", output = {S.longestPalindrome(s)}")
