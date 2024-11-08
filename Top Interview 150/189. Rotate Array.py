

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # Handle cases where k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]

def test(arr,s):
    for i in arr:
        print(f"input = {i[0]},k = {i[1]}")
        s.rotate(i[0], i[1])
        print(f"output = {i[0]}")

if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [[1, 1, 1, 2, 2, 3],3],
            [[0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3],5],
            [[2, 2, 1, 1, 1, 2, 2],3]
        ]
        test(tc,s)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            k = int(input())
            print(f"nums = {d},k = {k}")
            s.rotate(d, k)
            print(f" Output = {d}")