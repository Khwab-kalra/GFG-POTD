#Given a linked list, your task is to complete the function isLengthEven() which contains the head of the linked list, 
#and check whether the length of the linked list is even or not. Return true if it is even, otherwise false.

class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        count=0
        while(head):
            count+=1
            head=head.next
        if count%2==0:
            return True
        return False
