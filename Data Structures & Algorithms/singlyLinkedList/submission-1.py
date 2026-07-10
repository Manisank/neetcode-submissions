class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.linked_list = ListNode(val = None)
        self.head = self.linked_list
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next #we are not considering dummy here
        i = 0 
        while curr:
            if i == index:
                return curr.val
            i +=1 
            curr = curr.next

        # if index > i:
        return -1 


        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.tail == self.head:
            self.tail = new_node 
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        curr = self.head #we are  considering dummy here
        i = 0 
        while curr.next:
            if i == index:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return True
            i +=1 
            curr = curr.next

        # if index > i:
        return False 

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values 

        
