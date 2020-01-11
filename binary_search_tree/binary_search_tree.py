import sys
sys.path.append('./queue_and_stack')   # WORKS
# sys.path.append('../queue_and_stack') DOES NOT WORK
# sys.path.append('/Users/skutz/Documents/GitHub/Data-Structures/queue_and_stack') # WORKS
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if new value is less than current node
        if value < self.value:
            # there is NO self.left value
            if not self.left:
                # set NEW left chilas as new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)    
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)    


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True
        # target is smaller, go left
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                #return self.left.contains(target)
                sub_tree_contains = self.left.contains(target)        
        # target is larger, go right
        else: 
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)    
        # must return something
        return sub_tree_contains


    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        #  RECURSIVE SOLUTION
        # if we can go right, go right, until we cannot
        if not self.right:
            return self.value
        return self.right.get_max()

        # ITERATIVE SOLUTIONS
        # max_value = self.value    # don't need this
        # current_tree_root = self
        # while current_tree_root.right:
        #      current_tree_root = current_tree_root.right

        # return current_tree_root.value     

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return # no node to goto
        else:
            self.in_order_print(node.left) # go left as far as possible 
            print(node.value) # print whatever is there
            self.in_order_print(node.right) # passed left, now go right   

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # we need our Queue  O(n)
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node) # add current node to Queue
        while queue.len() > 0:
            cur_node = queue.dequeue() # remove first item in Queue
            print(cur_node.value) # print item taken form front of Queue
            if cur_node.left is not None: # if there is a L node
                queue.enqueue(cur_node.left) # add to queue
            if cur_node.right is not None: # if there is a R node
                queue.enqueue(cur_node.right) # add to queue  

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node) # push current node
        while stack.len() > 0:
            cur_node = stack.pop() 
            print(cur_node.value)
            if cur_node.left is not None:
                stack.push(cur_node.left)
            if cur_node.right is not None:
                stack.push(cur_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



bst = BinarySearchTree(5)
print(bst.contains(5))
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
