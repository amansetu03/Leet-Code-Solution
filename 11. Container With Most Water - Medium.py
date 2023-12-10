from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l<r:
            cw = min(height[l],height[r])*(r-l)
            ans = max(ans,cw)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans



def test(arr):
    s = Solution()
    for i in arr:
        print(f"number = \"{i}\",output = {s.maxArea(i)}")

if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    if x == '1':
        arr = [[1,8,6,2,5,4,8,3,7],[1,1]]
        test(arr)
    else:
        Sol = Solution()
        for _ in range(int(input())):
            height = [int(x) for x in input().split()]
            print(f"height = {height}, output = {Sol.maxArea(height)}")