class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pv = 0
        for i in s[::-1]:
            cv = d[i]
            if cv >= pv:
                ans += cv
            else:
                ans -= cv
            pv = cv
        return ans

def test(arr):
    s = Solution()
    for i in arr:
        print(f"s = \"{i}\",output = {s.romanToInt(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = ["III","LVIII","MCMXCIV"]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            s = input()
            print(f"height = {s}, output = {Sol.romanToInt(s)}")