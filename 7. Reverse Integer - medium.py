class Solution:
    def reverse(self, n: int) -> int:
        ans = 0
        f = False # flag for negative value
        if n < 0:
            f = True
            n = n * (-1)
        while n > 0:
            ans = ans * 10 + (n % 10)
            n = n // 10

        if f: ans *= -1 # if number was negative the convert ans into negative
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        if ans > ma or ans < mi:
            return 0
        return ans

def test(arr):
    s = Solution()
    for i in arr:
        print(f"number = \"{i}\", output = {s.reverse(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [130,-130,120,568]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            number = int(input())
            print(f"number = \"{number}\", output = {Sol.reverse(number)}")