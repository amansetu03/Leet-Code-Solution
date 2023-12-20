

class Solution:
    def reverse(self, n: int) -> int:# from Problem 7
        if n<0:
            return "---"
        ans = 0
        while n>0:
            ans = ans*10 + (n%10)
            n = n//10
        return ans
    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        if n == self.reverse(n):
            return True
        return False


def test(arr):
    s = Solution()
    for i in arr:
        print(f"number = \"{i}\",reverse = \"{s.reverse(i)}\" output = {s.isPalindrome(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [130,-130031,120,568,123321,-121,121]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            number = int(input())
            print(f"number = \"{number}\",reverse = \"{Sol.reverse(number)}\" output = {Sol.isPalindrome(number)}")