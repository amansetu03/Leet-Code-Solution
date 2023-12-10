from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fp = -1
        for i in range(len(nums)):
            if nums[i] == target:
                fp = i
                break
        if fp != -1:
            return [fp,fp+nums.count(target)-1]
        return [-1,-1]

def test(arr):
    s = Solution()
    for i in arr:
        print(f"number = \"{i}\",output = {s.searchRange(i[0],i[1])}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[[5,7,7,8,8,10],8],[[5,7,7,8,8,10],6],[[],0]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            nums = [int(x) for x in input().split()]
            target = int(input())
            print(f"nums = {nums},target = {target}, output = {Sol.searchRange(nums,target)}")