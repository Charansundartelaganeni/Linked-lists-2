

#TC: O(n) 
#SC: O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 


        lenA = 0 
        lenB = 0 

        p1 = headA #initially p1 points to headA
        p2 = headB #initially p2 points to headB

        while p1!=None: #finding the length of linked list A
            lenA+=1 
            p1 = p1.next 

        while p2!=None: #finding the length of linked list B
            lenB+=1 
            p2 = p2.next 

        pa = headA #pointer a points to headA
        pb = headB #pointer b points to headB

        while lenA>lenB: #place the pointer a by traversing through linked list A
            pa = pa.next 
            lenA-=1 
        while lenB>lenA: #place the pointer b by traversing through linked list A
            pb = pb.next 
            lenB-=1 

        while pa!=pb: #now traverse until both the pointers point the same node
            pa = pa.next  #increase pa by one
            pb = pb.next  #increase pb by one

        return pa #now return pa