from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for j in range(len(nums)):
            if nums[j]>=target:
                return j
        return j+1

def test(arr):
    s = Solution()
    for i in arr:
        print(f"nums  = {i[0]}, target = {i[1]},output = {s.searchInsert(i[0],i[1])}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[[1,3,5,6],5],[[1,3,5,6],2],[[1,3,5,6],7]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            L =[int(x) for x in input().split()]
            val = int(input())
            print(f"nums  = {L}, val = {val}, output = {Sol.searchInsert(L, val)}")