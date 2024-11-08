# def findS(k,n,w):
#     cost = 0
#     for i in range(1,w+1):
#         cost += (k*i)
#     b = cost - n
#     return b if b>0 else 0
#
# k,n,w = [int(s) for s in input().split()]
# print(findS(k,n,w))

def print_p(n,m):
    f = True
    for i in range(1,n+1):
        if i %2 != 0:
            print("#"*m)
        else:
            if f:
                print(f"{'.'*(m-1)}#")
                f = False
            else:
                print(f"#{'.'*(m-1)}")
                f = True
print_p(3,3)
print()
print_p(3,4)
print()
print_p(5,3)
print()
print_p(9,9)