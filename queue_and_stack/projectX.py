# How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length of the list. If the list is even, you should return the first of the two "middle" nodes. You may not store the nodes in another data structure.
class Node:
  def __init__(self,val):
    self.value = val
    self.next = None
    self.index = None

class LinkedList:
    def __init__(self):
      self.head = None

    def set_head(self,val):
      self.head = Node(val)
      self.head.index = 0

    def display(self):
      n = self.head
      while n != None:
        print(n.value)
        print('index', n.index)
        n = n.next

    def attach_end(self,val):
      i = self.head.index
      new_node = Node(val)
      n = self.head
      while n.next:
        n = n.next
        i = i + 1
    
      print('n', n.value)
      print('new_node', new_node.value)
      new_node.index = i + 1
      n.next = new_node

      
ll = LinkedList()
ll.set_head(20)
ll.attach_end(21)
ll.attach_end(22)
ll.attach_end(23)
ll.display()