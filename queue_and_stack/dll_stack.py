import sys
# sys.path.append('../doubly_linked_list')  
sys.path.append('/Users/skutz/Documents/GitHub/Data-Structures/doubly_linked_list') 
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.value = None
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # if(self.size > 0):
        if(self.storage.tail):
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None    

    def len(self):
        return self.size

st = Stack()
st.push(100)
st.push(101)
st.push(105)
print(st.len())
print(st.pop())
print(st.len())

    #    self.s.push(100)
    #     self.s.push(101)
    #     self.s.push(105)
    #     self.assertEqual(self.s.pop(), 105)
    #     self.assertEqual(self.s.len(), 2)
