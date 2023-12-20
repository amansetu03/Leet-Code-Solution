from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        for i in range(len(digits)-1,-1,-1):
            cs = digits[i]+c
            digits[i] = cs%10
            c = cs//10
        if c:
            digits.insert(0,c)
        return digits

def test(tc):
    s = Solution()
    for i in tc:
        print(f"digits = \"{i}\", output = {s.plusOne(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [1, 2, 3],
            [4, 3, 2, 1],
            [9]
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            print(f"disit = \"{d}\", output = {s.plusOne(d)}")