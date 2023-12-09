class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        temp = ""
        ans = 0
        for i in s:
            if i in temp:
                index = temp.index(i)
                temp = temp[index+1:]
            temp+=i
            ans = max(ans,len(temp))
        return ans

def test(arr):
    S = Solution()
    for i in arr:
        print(f"s = '{i}', your output = {S.lengthOfLongestSubstring(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = ["abcabcdabcbb","bbbbbb","pwwkew","khtfturd"]
        test(arr)
    else:
        S = Solution()
        for _ in range(int(input())):
            s = input()
            print(f"s = '{s}', output = {S.lengthOfLongestSubstring(s)}")
