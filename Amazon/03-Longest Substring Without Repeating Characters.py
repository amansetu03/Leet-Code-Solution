"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Topics - Hash Table, String, Sliding Window

Hints- Generate all possible substrings & check for each substring if it's valid and keep updating maxLen accordingly.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        start = 0
        index_map = {}
        ans = 0
        for end in range(n):
            if s[end] in index_map and index_map[s[end]] >= start:
                start = end + 1
            index_map[s[end]] = end
            ans = max(ans,end - start + 1)
        return ans

if __name__ == "__main__":
    t = int(input("Enter number of test: "))
    S = Solution()
    for _ in range(t):
        s = input()
        print(S.lengthOfLongestSubstring(s))
        