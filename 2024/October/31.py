'''
Insert in Sorted way in a Sorted DLL
------------------------------------
Given a sorted doubly linked list and an element x, you need to insert the element x into the correct position 
in the sorted Doubly linked list(DLL).
Note: The DLL is sorted in ascending order'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        #code here
        ans = head
        if head.data>=x:
            head.prev = Node(x)
            head.prev.next=head
            ans = head.prev
            return ans
        while(head.next):
            if head.data<=x and head.next.data>x:
                tmp=head.next
                head.next = Node(x)
                head.next.prev = head
                head.next.next = tmp
                tmp.prev = Node(x)
                return ans
            head=head.next
        if head.data<=x:
            head.next = Node(x)
            head.next.prev = head
        return ans
