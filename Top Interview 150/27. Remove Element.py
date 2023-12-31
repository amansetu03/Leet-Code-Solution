from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return right
def test(arr):
    s = Solution()
    for i in arr:
        print(f"nums  = {i[0]}, val = {i[1]},output = {s.removeElement(i[0],i[1])}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[[3,2,2,3],3],[[0,1,2,2,3,0,4,2],2]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            L =[int(x) for x in input().split()]
            val = int(input())
            print(f"nums  = {L}, val = {val}, output = {Sol.removeElement(L,val)}")