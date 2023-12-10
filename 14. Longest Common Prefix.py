from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for i in strs:
            for j in range(len(s)):
                if i.count(s) == 0:
                    s = s[:len(s) - 1]
        return s

def test(arr):
    s = Solution()
    for i in arr:
        print(f"s = \"{i}\",output = \"{s.longestCommonPrefix(i)}\"")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [["flower","flow","flight"],["dog","racecar","car"]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            s = [x for x in input().split()]
            print(f"strs = {s}, output = \"{Sol.longestCommonPrefix(s)}\"")