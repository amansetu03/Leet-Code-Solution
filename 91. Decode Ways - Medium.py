class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            if one_digit != 0:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

def test(arr):
    s = Solution()
    for i in arr:
        print(f"input = {i}, output = {s.numDecodings(i)}")

if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            "12",
            "226",
            "06"
        ]
        test(tc)
    else:
        print("Enter no. of tc")
        for _ in range(int(input())):
            d = input("Enter string")
            print(f"disit = \"{d}\", output = {s.numDecodings(d)}")

