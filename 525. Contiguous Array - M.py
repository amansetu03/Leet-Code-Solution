from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sv = 0
        maxLength = 0
        for i,val in enumerate(nums):
            sv += 1 if val == 1 else -1
            if sv == 0:
                maxLength = i + 1
            elif sv in mp:
                maxLength = max(maxLength, i - mp[sv])
            else:
                mp[sv] = i
        return maxLength



def test(arr,S):
    for i in arr:
        print(f'input = {i}, Output = {S.findMaxLength(i)}')
if __name__ == "__main__":
    print("enter 1 for test and 2 for run")
    x = input("")
    Sol = Solution()
    if x == '1':
        arr = [[0, 1],[0, 1, 0], [0, 1, 0, 1]]
        test(arr,Sol)
    else:
        print("Enter number of test case")
        for _ in range(int(input())):
            L = [int(x) for x in input().split()]
            print(f"nums  = {L}, output = {Sol.findMaxLength(L)}")