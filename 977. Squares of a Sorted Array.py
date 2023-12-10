from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        i = r
        ans = [0]*n
        while l <= r:
            lv, rv = nums[l]**2,nums[r]**2
            if lv > rv:
                ans[i] = lv
                l += 1
            else:
                ans[i] = rv
                r -= 1
            i -= 1
        return ans

def test(arr):
    s = Solution()
    for i in arr:
        print(f"nums = {i}, output = {s.sortedSquares(i)}")

if __name__ == "__main__":
    n = input("enter 1 for test 2 for run")
    s = Solution()
    if n == "1":
        arr = [[-4,-1,0,3,10],[-7,-3,2,3,11]]
        test(arr)
    else:
        for _ in range(int(input())):
            nums = [int(x) for x in input().split()]
            print(f"nums = {nums}, output = {s.sortedSquares(nums)}")
