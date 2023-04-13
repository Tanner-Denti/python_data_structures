'''
Min Heap rules:
1) Conceptually a heap is a binary tree, but it's implemented as an array / list.
2) Any parent/non-leaf node must be less than or equal to its' children (Root is smallest, opposite for max heap).
3) The tree should be "complete" except for perhaps the right-most leaf nodes (All nodes on the leaf level are shifted left).
'''
import math
from multipledispatch import dispatch

'''
TODO
- Modify is_heap so that it runs an algorithm to ensure the heap is following heap rules.
- Create heap_sort_descending()
- Incorporate dunder methods
- Figure out how to make the class iterable (consider inheriting from list?)
- Figure out how to make the class work with ints, floats, strings (maybe others).
- More thoroughly analyze space and time complexity and include it in all user method doc strings.
'''

class MinHeap():
    ''' Viable min heap of integers. '''
    def __init__(self, items: list[int] = [])-> None:
        ''' Implement our heap. It can be constructed from a given list. '''
        if items.__len__() == 0:
            self._items: list[int] = []
        else:
            self._items: list[int] = items.copy()
        
        self.build_heap() # Reorganize self._items into a heap.
        self.is_heap = True
    
    # -------------------- Properties --------------------
    @property
    def size(self) -> int:
        ''' Get the length of the heap. '''
        return self._items.__len__()
    
    @property
    def is_empty(self) -> bool:
        ''' Return a boolean value: true if the heap is empty, else false. '''
        return self.size == 0
    
    @property
    def height(self) -> int:
        ''' Get the number of edges between the root and the lowest leaf of the heaps' tree representation. '''
        return math.log2(self.size).__int__() if self.size > 0 else 0 # 0 is not in the domain of the log function.
    
    @property
    def is_heap(self) -> bool:
        ''' Return a boolean value: true if the heap is valid, else valse. '''
        return self._is_heap

    @is_heap.setter
    def is_heap(self, state: bool):
        ''' Set the value of _is_heap. '''
        self._is_heap = state

    # -------------------- User methods --------------------
    def build_heap(self) -> None:
        ''' Build / restore a heap "in place" in O(n) time. '''
        for i in range(self._last_subtree_index(), -1, -1):
            self._heapify_down(i)
            
        self.is_heap = True

    def heap_sort_ascending(self) -> None:
        ''' Sort the heap "in place" via heap sort in O(nlogn) time. '''
        self.build_heap() 
        for i in range(self.size - 1, -1, -1):
            self._move_min_to_end(i)
        
        # If it's sorted by ascending order it will remain a min heap.
        self.is_heap = True

    @dispatch(int)
    def insert(self, item: int) -> None:
        ''' Add a value to the heap. It will be placed according to heap rules. '''
        self._items.append(item)
        self._heapify_up()
    
    @dispatch(list)
    def insert(self, items: list) -> None:
        ''' Add a list of values to the heap. Each item in the list will be placed according to heap rules. '''
        for item in items:
            self._items.append(item)
            self._heapify_up()
        
    @dispatch()
    def extract_min(self) -> int:
        ''' Remove and return the value of the root node from the heap. '''
        if self.size == 0: 
            raise Exception("IdexError: The size of 'self._items' must be greater than zero.")
        # Save off the root node.
        root = self._items[0]
        # Replace the root node with the last node inserted, then re-order.
        self._items[0] = self._items[self.size - 1]
        self._items.pop()
        self._heapify_down(0)
        return root
    
    @dispatch(int)
    def extract_min(self, last_heapify_index: int) -> int:
        ''' Remove and return the value of the root node from the heap. '''
        if self.size == 0: 
            raise Exception("IdexError: The size of 'self._items' must be greater than zero.")
        # Save off the root node.
        root = self._items[0]
        # Replace the root node with the last node in the heap, then re-order.
        self._items[0] = self._items[last_heapify_index]
        self._items.pop(last_heapify_index)
        last_heapify_index -= 1 # List is 1 element smaller so adjust the index.
        self._heapify_down(0, last_heapify_index)
        return root
    
    def get_min(self) -> int:
        ''' Read the value of the root node. '''
        if self.size == 0: 
            raise Exception("IdexError: The size of 'self._items' must be greater than zero.")
        return self._items[0]

    def clear(self):
        ''' Remove all values from the heap. '''
        self._items.clear()
        
    def get_items_as_list(self):
        ''' Returns the values in the heap as a list. '''
        return self._items.copy()
    
    # -------------------- Private / Helper methods --------------------
    @dispatch(int)
    def _heapify_down(self, index: int) -> None:
        ''' Sort a heap node downward into its' proper position according to heap rules. ''' 
        while self._has_left_child(index):
            # Find the smallest child between left and right.
            smaller_child_index = self._get_left_child_index(index)
            if self._has_right_child(index) and self._right_child(index) < self._left_child(index):
                smaller_child_index = self._get_right_child_index(index)

            # If there is a child that is smaller, swap, else break.
            if self._items[index] > self._items[smaller_child_index]:
                self._swap(index, smaller_child_index)
                index = smaller_child_index
            else:
                break
    
    @dispatch(int, int)
    def _heapify_down(self, index: int, end_index: int) -> None:
        ''' Sort a heap node downward into its' proper position according to heap rules. '''
        while self._has_left_child(index) and self._get_left_child_index(index) <= end_index:
            
            # Find the smallest valid child between left and right.
            smaller_child_index = self._get_left_child_index(index)
            if self._has_right_child(index) and \
                self._right_child(index) < self._left_child(index) and \
                self._get_right_child_index(index) <= end_index:
                
                smaller_child_index = self._get_right_child_index(index)
            
            # If there is a valid smaller child, swap, else break.
            if self._items[index] > self._items[smaller_child_index]:     
                self._swap(index, smaller_child_index)
                index = smaller_child_index
            else:
                break
            
    
    def _heapify_up(self) -> None:
        ''' Sort the last item in the heap upward into its proper position according to heap rules. '''
        index = self.size - 1
        while self._has_parent(index) and self._parent(index) > self._items[index]:
            self._swap(self._get_parent_index(index), index)
            index = self._get_parent_index(index)
    
    def _swap(self, index_one:int, index_two:int) -> None:
        ''' Switch the values of two "nodes". '''
        self._items[index_one], self._items[index_two] = self._items[index_two], self._items[index_one]

    def _last_subtree_index(self) -> int:
        ''' Get the index for the root of the lowest, rightmost subtree (not a leaf). '''
        return (self.size // 2) -1 if (self.size > 0) else 0
    
    def _move_min_to_end(self, last_heapify_index: int) -> None:
        ''' Move the minimum value to the end of the list. '''
        min_value = self.extract_min(last_heapify_index)
        self._items.append(min_value)
    
    def _get_left_child_index(self, parent_index: int) -> int:
        ''' Gives the left child index based on heap rules. '''
        return (parent_index * 2) + 1
    
    def _get_right_child_index(self, parent_index: int) -> int:
        ''' Gives the right child index based on heap rules. '''
        return (parent_index * 2) + 2
    
    def _get_parent_index(self, child_index: int) -> int:
        ''' Gives the parent index of any child "node". '''
        return (child_index - 1) // 2
    
    def _has_left_child(self, index: int) -> bool:
        ''' Returns true if the calculated left child index size is less than the actual size of the heap, otherwise returns false. '''
        return self._get_left_child_index(index) < self.size

    def _has_right_child(self, index: int) -> bool:
        ''' Returns true if the calculated right child index size is less than the actual size of the heap, otherwise returns false. '''
        return self._get_right_child_index(index) < self.size

    def _has_parent(self, index: int) -> bool:
        ''' Returns True if the parent index is greater than or equal to zero. '''
        return self._get_parent_index(index) >= 0
    
    def _left_child(self, index: int) -> int:
        ''' Return the value of the left child if any. '''
        if self._has_left_child(index):
            return self._items[self._get_left_child_index(index)]
        raise Exception("IndexError: Please enter an index for which a left child node exists (Should be less than the length of 'self._items').")
    
    def _right_child(self, index: int) -> int:
        ''' Return the value of the right child if any. '''
        if self._has_right_child(index):
            return self._items[self._get_right_child_index(index)]
        raise Exception("IndexError: Please enter an index for which a right child node exists (Should be less than the length of 'self._items').")

    def _parent(self, index: int) -> int:
        ''' Return the value of the parent node if any. '''
        if self._has_parent(index):
            return self._items[self._get_parent_index(index)]
        raise Exception("IndexError: Please enter an index for which a parent node exists (Should be less than the length of 'self._items').")
    

    




    

    


    

