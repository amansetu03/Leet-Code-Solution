from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            if prev.next == current:
                prev = prev.next
            else:
                prev.next = current.next

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

def test(arr):
    for i in arr:
        ll1 = arrayToList(i)
        S = Solution()
        print("LL = ",end = " ")
        display(ll1)
        oh = S.deleteDuplicates(ll1)
        print("output = ", end=" ")
        display(oh)

if __name__ == "__main__":
    s = Solution()
    n = input("enter 1 to pd-tc 2 for manual-tc ")
    if n == "1":
        tc = [
            [1,2,3,3,4,4,5],
            [1,1,1,2,3],
            [0,0,0,1,2,3,3,3,4,5,5,5,5,6,6,6,6,6]
        ]
        test(tc)
    else:
        for _ in range(int(input())):
            d = [int(x) for x in input().split()]
            ll1 = arrayToList(d)
            print("LL = ", end=" ")
            display(ll1)
            oh = s.deleteDuplicates(ll1)
            print("output = ", end=" ")
            display(oh)

