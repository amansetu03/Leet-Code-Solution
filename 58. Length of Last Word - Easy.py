class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        x=s.split(" ")
        return len(x[-1])
    def lengthOfLastWord2(self,s: str) -> int:
        l = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                l+=1
            elif l>0:
                break
        return l
def test(tc):
    s = Solution()
    for i in tc:
        print(f"s = \"{i}\", output = {s.lengthOfLastWord(i)}")
if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = ["Hello World","   fly me   to   the moon  ","luffy is still joyboy"]
        test(tc)
    else:
        for _ in range(int(input())):
            word = input()
            print(f"s = \"{word}\", output = {s.lengthOfLastWord2(word)}")