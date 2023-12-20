from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c, i = 0, 0
        while i < len(nums):
            if c == 0 or c == 1 or nums[c-2] != nums[i]:
                nums[c] = nums[i]
                c += 1
            i += 1
        return c
def test(tc):
    s = Solution()
    for i in tc:
        print(f"nums = {i}, output = {s.removeDuplicates(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [1,1,1,2,2,3],
            [0,0,1,1,1,1,2,3,3],
            [0,0,0,1,2,3,3,3,4,5,5,5,5,6,6,6,6,6]
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            print(f"nums = {d}, Output = {s.removeDuplicates(d)}")