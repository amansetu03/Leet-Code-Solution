from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        m = 0

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                m += 1
                l += 1
            elif nums[m] == 2:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
            else:
                m += 1


def test(tc):
    s = Solution()
    for i in tc:
        print(f"nums = {i}")
        s.sortColors(i)
        print(f"Output = {i}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [2, 0, 2, 1, 1, 0],
            [2,0,1],
            [1,0,2,0,1,2,0]
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            print(f"nums = {d}")
            s.sortColors(d)
            print(f"Output = {d}")