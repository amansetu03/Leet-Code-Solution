class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n

        # if n == 0:
        #     return 1
        # ans = 1
        # for i in range(abs(n)):
        #     ans *= x
        # if n<0:
        #     return 1/ans
        # return float(ans)

        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)
def test(arr):
    s = Solution()
    for i in arr:
        print(f"x  = {i[0]}, n = {i[1]},output = {s.myPow(i[0],i[1])}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[2.00000,10],[2.10000,3],[2.00000,-2]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            x = float(input())
            n = int(input())
            print(f"nums  = {x}, val = {n}, output = {Sol.myPow(x, n)}")