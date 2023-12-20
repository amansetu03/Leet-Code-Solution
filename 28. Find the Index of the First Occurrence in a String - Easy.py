class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=0
        for i in range(len(haystack)):
            if haystack[i]==needle[0] and j==0:
                ans = i
                j+=1
            elif haystack[i]==needle[j]:
                j+=1
            else:
                j=0
            if j==len(needle):
                return ans
        return -1
#--------- This is the another solution using slising of the string. -----------#
    def strStr2(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

def test(arr):
    s = Solution()
    for i in arr:
        print(f"string = \"{i[0]}\", needle = \"{i[1]}\",output = {s.strStr(i[0],i[1])}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [["sadbutsad","sad"],["leetcode","leeto"]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            h = input()
            n = input()
            print(f"string = \"{h}\", needle = \"{n}\",output = {Sol.strStr(h, n)}")