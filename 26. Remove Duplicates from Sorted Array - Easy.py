from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        n = len(nums)
        for i in range(n):
            if nums[ptr - 1] != nums[i]:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr
def test(arr):
    s = Solution()
    for i in arr:
        print(f"nums  = {i},output = {s.removeDuplicates(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[1,1,2],[0,0,1,1,1,2,2,3,3,4],[1,1,2,2,2,3,5,6]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            s = [int(x) for x in input().split()]
            print(f"nums  = {s}, output = {Sol.removeDuplicates(s)}")