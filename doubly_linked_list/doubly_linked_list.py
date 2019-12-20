"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)
    #   return 'ListNode( val: {!r}, prev: {!r}, next: {!r}'.format(self.value, self.prev, self.next)

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        print("length is: ", self.length)
        return self.length

    # def __str__(self):
    #   if self.head is None and self.tail is None:
    #     return "empty"
    #   curr_node = self.head
    #   output = ''
    #   output += str(curr_node) + ' <-> '
    #   while curr_node.next is not None:
    #     curr_node = curr_node.next
    #     output += str(curr_node) + ' <-> '
    #   return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
      new_node = ListNode(value)
      self.length += 1
      if self.head is None and self.tail is None:
        # empty list case
        self.head = new_node 
        self.tail = new_node
      else:
        # save the old head to local var
        old_head = self.head
        # link both nodes together
        new_node.next = old_head
        old_head.prev = new_node
        # assign head to the new node
        self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
      if self.head is None:
        return

      node_to_remove = self.head
      new_head = node_to_remove.next
      # move head pointer to the next value
      self.head = new_head
      # sever the connection to node_to_remove
      node_to_remove.next = None
      self.length -= 1

      if self.head is None:
        self.tail = None
      else:
        self.head.prev = None

      val = node_to_remove.value
      # del node_to_remove

      return val

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
        # empty list case
            self.head = new_node 
            self.tail = new_node
        else:
        # save the old TAIL to local var
            old_tail = self.tail
        # link both nodes together
            new_node.prev = old_tail
            old_tail.next = new_node
        # assign head to the new node
            self.tail = new_node
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""     
    def remove_from_tail(self):
    #     if self.tail is None:
    #         return

    #     tail_node_to_remove = self.tail
    #     new_tail = tail_node_to_remove.prev
    #     # move head pointer to the next value
    #     self.tail= new_tail
    #     # sever the connection to tail_node_to_remove
    #     tail_node_to_remove.prev = None
    #     self.length -= 1

    #     if self.head is None:
    #         self.tail = None
    #     else:
    #         # self.tail.next = None  # original NOPE
    #         # self.tail = new_tail.next  # original NOPE

    #     #val = tail_node_to_remove.value
    #     # del node_to_remove

    #     return val

        # THIS WORKS BETTER, something buggy above from lecture code LINE 141
        value = self.tail.value
        self.delete(self.tail)
        return value


    # def delete(self):
    #     if self.prev:
    #         self.prev.next = self.next
    #     if self.next:
    #         self.next.prev = self.prev


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
          return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
          return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
          return
        if self.head == self.tail:
          self.head = None
          self.tail = None
          self.length -=1
        elif self.head == node:
          self.head = node.next
          self.length -= 1
          node.delete()
        elif self.tail == node:
          self.tail = node.prev
          self.length -= 1
          node.delete()
        else:
          self.length -= 1
          node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None:
            return None
        curr_node = self.head
        max_val = -float("inf")
        if curr_node is None:
            return None
        while curr_node is not None:
            if curr_node.value > max_val:
                max_val = curr_node.value
            curr_node = curr_node.next
        return max_val


# dll = DoublyLinkedList()

# dll.add_to_head(10)
# dll.add_to_head(20)
# dll.add_to_head(-10)
# print(dll)
# len(dll)
# print(dll.remove_from_head())
# print(dll)
# len(dll)
# print(dll.get_max())

# dll.add_to_tail(0)
# dll.add_to_tail(1)
# dll.add_to_tail(-2)
# print(dll)
# len(dll)
# # print(len(dll))    

################
# ll.add_to_head(1)
# ll.print_list()
# ll.add_to_head(2)
# ll.add_to_head(3)
# ll.print_list()
# print(len(ll))
# ll.delete(first_node)
# ll.print_list()


##################
# """Each ListNode holds a reference to its previous node
# as well as its next node in the List."""


# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     # # make helpful __str__
#     # def __str__(self):
#     #     # return 'ListNode( val: {!r}, prev: {!r}, next: {!r}'.format(self.value, self.prev, self.next)
#     #     return str(self.value)

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""
#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""
#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""
#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""


# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         # print("length is: ", self.length)
#         return self.length

#     def __str__(self):
#         if self.head is None and self.tail is None:
#             return "empty"
#         curr_node = self.head
#         output = ''
#         output += str(curr_node) + ' <-> '
#         while curr_node.next is not None:
#             curr_node = curr_node.next
#             output += str(curr_node) + ' <-> '
#         return output

#     # start printing at HEAD     
#     def print_list(self):
#         curr_node = self.head
#         while curr_node is not None:
#             print("\t node: ", curr_node)
#             curr_node = curr_node.next    


#     """Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly."""
#     def add_to_head(self, value):
#         if self.head is None:
#             node = ListNode(value)
#             self.tail = node
#             self.head = node
#         else:
#             current_node = self.head
#             current_node.insert_before(value)
#             self.head = current_node.prev

#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""
#     def remove_from_head(self):
#         current_node = self.head
#         self.head = current_node.next
#         current_node.delete()
#         return current_node.value

#     """Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly."""
#     def add_to_tail(self, value):
#         if self.head is None:
#             node = ListNode(value)
#             self.head = node
#             self.tail = node
#         else:
#             current_tail = self.tail
#             current_tail.insert_after(value)
#             self.tail = current_tail.next

#     """Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""
#     def remove_from_tail(self):
#         current_node = self.tail
#         self.tail = current_node.prev
#         current_node.delete()
#         return current_node.value

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List."""
#     def move_to_front(self, node):
#         if self.tail == node:
#             self.tail = node.prev
#         node.delete()
#         self.add_to_head(node.value)

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List."""
#     def move_to_end(self, node):
#         if self.head == node:
#             self.head = node.next
#         node.delete()
#         self.add_to_tail(node.value)

#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""
#     def delete(self, node):
#         if node == self.head:
#             self.head = node.next
#         elif node == self.tail:
#             self.tail = node.prev
#         node.delete()
#         return node.value

        
#     """Returns the highest value currently in the list"""
#     def get_max(self):
#         if self.head is None:
#             return None
#         curr_node = self.head
#         max_val = -float("inf")
#         if curr_node is None:
#             return None
#         while curr_node is not None:
#             if curr_node.value > max_val:
#                 max_val = curr_node.value
#             curr_node = curr_node.next
#         return max_val

# first_node = ListNode(100)
# ll = DoublyLinkedList(first_node)
# ll.print_list()

# #  Noooo
# # ll.add_to_head(ListNode(200))
# # ll.print_list()


# ll.add_to_head(1)
# ll.print_list()
# ll.add_to_head(2)
# ll.add_to_head(3)
# ll.print_list()
# print(len(ll))
# ll.delete(first_node)
# ll.print_list()