class Solution:
    def decipherAstroMassege(self,n,digit:str) -> str:
        keyMap = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
            0:[' ']
        }
        x=0
        stack = []
        message = ""
        c = 0
        for i in digit:
            if i == '*':
                message += keyMap[stack[-1]][c]
                stack.pop()
                continue
            if c > 2:
                if i == '7' or i == '9':
                    if c==3:
                        message += keyMap[stack[-1]][c]
                        stack.pop()
                        c=1
                        print("KKKKKKKKk")
                        continue
                else:
                    message += keyMap[stack[-1]][c-1]
                    c = 1
                    stack.pop()


            i = int(i)
            if not stack:
                stack.append(i)
            elif i == stack[-1]:
                c += 1
            elif i != stack[-1]:
                message += keyMap[stack[-1]][c]
                stack.pop()
                stack.append(i)
                c = 0

            print(c)
            print(message)
            print(stack)
            print("-----------------",i)
        if c>2:
            if i == '7' or i == '9':
                if c==3:
                    message += keyMap[stack[-1]][c]
                    c=1
            else:
                message += keyMap[stack[-1]][c-1]
                x = c // 3
                c = c%3

        if c>=0:
            if x>=0:
                message += keyMap[stack[-1]][c]*(x+1)
            else: message += keyMap[stack[-1]][c]
        return message
if __name__ == "__main__":
    S = Solution()
    # print(S.decipherAstroMassege(10,"7555266338"))
    print(S.decipherAstroMassege(23,"225552*22255044666555555330777777777777733555555555555"))