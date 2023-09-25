class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1:ListNode,l2:ListNode)->ListNode:
        num1=0
        num2=0
        i=0
        while l1!=None:
            num1=num1+l1.val*10**i
            i+=1
            l1=l1.next
        i=0
        while l2!=None:
            num2=num2+l2.val*10**i
            i+=1
            l2=l2.next
        num3num=num1+num2
        num3=list(str(num3num))
        num3.reverse()
        
        
        head=ListNode(num3num,None)
        l3=head
        for i in range(len(num3)-1):
            l3.val=int(num3[i])
            l3.next=ListNode(int(num3[i+1]),None)
            l3=l3.next
        return(head)



class ListNode(self,val=0,next=None):
    def __init__(val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    