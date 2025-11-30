class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            print(f"total is {total}")

            carry = total // 10
            print(f"carry is {carry}")
            print(f"next value {total % 10}")
            curr.next = ListNode(total % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for i in values:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

#l1 = build_linked_list([2,4,3])
#l2 = build_linked_list([5,6,4])
l1 = build_linked_list([9,9,9,9,9,9,9])
l2 = build_linked_list([8,9,9,9,0,0,0,1])

sl = Solution()
rs = sl.addTwoNumbers(l1, l2)

print(linked_list_to_list(rs))

