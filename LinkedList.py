class NodeList:
    def __init__(self,val = 0,next=None):
        self.val = val
        self.next = next

a = NodeList(1)
b = NodeList(2) 
c = NodeList(3)
d = NodeList(4)
e = NodeList(5)
a.next = b
b.next = c  
c.next = d
d.next = e
head = a

def printLL(head):
    while head:
        print(head.val,"next =",head.next)
        head = head.next

# printLL(head)

def insertAtHead(head,val):
    new_node =  NodeList(val)
    new_node.next = head
    head = new_node
    while head:
        print(head.val)
        head = head.next
# insertAtHead(head,0)

def insertAtEnd(head,val):
    current = head
    end_node = NodeList(val)
    while current.next:
        current = current.next
    current.next = end_node
    while head:
        print(head.val)
        head = head.next
# insertAtEnd(head,4)

def updateNode(head,val):
    current = head
    while current:
        if current.val == val:
            current.val = val*2
            break
        current = current.next
    while head:
        print(head.val)
        head = head.next

# updateNode(head,2)

def updateNodeByPosition(head,pos,val):
    
    current = head
    index = 0
    while current:
        if index == pos:
            current.val = val
            break
        index+=1
        current = current.next
    while head:
        print(head.val)
        head = head.next

# updateNodeByPosition(head,2,10)


def deleteNode(head):
    current = head
    while current:
        if current.next.val == 2:
            current.next = current.next.next
            break
        current = current.next
    while head:
        print(head.val)
        head = head.next

# deleteNode(head)

def fastandSlow(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(fastandSlow(head))

def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow== fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        