from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = 0
        for i in nums:
            if g < 0:
                return False
            elif i > g:
                g = i
            g -= 1
        return True


def test(tc):
    s = Solution()
    for i in tc:
        print(f"nums = {i} output = {s.canJump(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [2, 0, 2, 1, 1, 0],
            [2,0,1],
            [1,0,2,0,1,2,0],
            [2, 3, 1, 1, 4],
            [3,2,1,0,4]
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            print(f"nums = {d}")

            print(f"Output = {s.canJump(d)}")