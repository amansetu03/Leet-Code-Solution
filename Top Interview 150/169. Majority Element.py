from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        ans = 0
        for i in nums:
            if c==0:
                ans=i
            if i == ans:
                c+=1
            else:
                c-=1
        return ans

def test(arr,s):
    for i in arr:
        print(f"input = {i} output = {s.majorityElement(i)}")

if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [1, 1, 1, 2, 2, 3],
            [0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3],
            [2, 2, 1, 1, 1, 2, 2]
        ]
        test(tc,s)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            print(f"nums = {d}, Output = {s.majorityElement(d)}")