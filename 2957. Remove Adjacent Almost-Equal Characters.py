class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        op = 0
        i = 0
        n = len(word)
        while i < n:
            count = 1
            while i + 1 < n and (word[i] == word[i + 1] or abs(ord(word[i]) - ord(word[i + 1])) == 1):
                count += 1
                i += 1
            op += count // 2
            i += 1
        return op

def test(tc):
    s = Solution()
    for i in tc:
        print(f"word = {i}, output = {s.removeAlmostEqualCharacters(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = ["aaaaa","abddez","zyxyxyz"]
        test(tc)
    else:
        for _ in range(int(input())):
            word = input()
            print(f"word = {word}, output = {s.removeAlmostEqualCharacters(word)}")
