class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val: 
                tail.next = current2
                current2 = current2.next
            else:
                tail.next = current1
                current1 = current1.next

            tail = tail.next
        if current1:
            tail.next = list1
        if current2: 
            tail.next = list2
        
        return dummy.next

        def mergeTwoListsRecursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
