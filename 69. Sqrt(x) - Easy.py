
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        r = x
        while r > x / r:
            r = (r + x // r) // 2
        return r
def test(tc):
    s = Solution()
    for i in tc:
        print(f"x = \"{i}\", output = {s.mySqrt(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            4,
            8,
            9
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            d = int(input())
            print(f"disit = \"{d}\", output = {s.mySqrt(d)}")