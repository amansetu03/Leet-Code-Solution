from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x+y+carry

            carry = total//10
            current.next = ListNode(total%10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next
        return dummy.next


def insert(root, item):
    temp = ListNode(item)
    if (root == None):
        root = temp
    else:
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
    return root

def display(ll):
    h = ll
    if h is None:
        print("None")
    while h is not None:
        print(f"{h.val}-->",end="")
        h = h.next
    print(None)

def arrayToList(arr):
    root = None
    for i in range(0,len(arr)):
        root = insert(root, arr[i])

    return root

def test():
    ll1 = arrayToList([2,4,3])
    ll2 = arrayToList([5,6,4])
    S = Solution()
    oh = S.addTwoNumbers(ll1, ll2)
    display(ll1)
    display(ll2)
    display(oh)

print("enter 1 for test and 2 for run")
x = input("")
if x == '1':
    test()
else:
    t = int(input())
    for _ in range(t):
        l1 = [int(x) for x in input().split()]
        l2 = [int(x) for x in input().split()]

        ll1 = arrayToList(l1)
        ll2 = arrayToList(l2)
        S = Solution()
        oh = S.addTwoNumbers(ll1,ll2)
        h = oh
        output = []
        while h is not None:
            output.append(h.val)
            h = h.next
        print(f"l1 = {l1}, l2 = {l2}, output = {output}")

        display(ll1)
        display(ll2)
        display(oh)